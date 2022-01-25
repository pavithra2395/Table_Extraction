import cx_Oracle

from .error_row_model import ErrorRow


class DBManager:
    con = None
    cur = None
    isError = False

    def __init__(self, user, password, dsn, encoding):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.encoding = encoding

    def connection(self):
        try:
            self.con = cx_Oracle.connect(user=self.user, password=self.password, dsn=self.dsn, encoding=self.encoding)
            return self.con
        except cx_Oracle.DatabaseError as er:
            print('There is an error in Oracle database connection:', er)
            return None

    def cursor(self):
        if self.con is None:
            return
        self.cur = self.con.cursor()

    def isConnected(self):
        return self.con is not None

    def save(self, query):
        try:
            self.connection()
            if self.isConnected():
                self.cursor()
                self.cur.execute(query)
        except cx_Oracle.Error as e:
            error_obj, = e.args
            print(f'\nerror is :{error_obj.message} \n {e}')
            self.isError = True
        except cx_Oracle.IntegrityError as ie:
            print("Integrity error: ", ie)
        else:
            self.commit()

    def saveAll(self, query, rows):
        try:
            self.connection()
            if self.isConnected():
                self.cursor()
                self.cur.executemany(query, rows, batcherrors=True, arraydmlrowcounts=True)
        except cx_Oracle.Error as e:
            error_obj, = e.args
            print(f'\nerror is :{error_obj.message} \n {e}')
            self.isError = True
        except cx_Oracle.IntegrityError as ie:
            print("Integrity error: ", ie)
        else:
            self.commit()
        try:
            self.stats = Stats(self.cur.getbatcherrors(), self.cur.getarraydmlrowcounts())
        except Exception as e:
            print(e)

    def fetchAll(self, query):
        try:
            self.connection()
            if self.isConnected():
                self.cursor()
                self.cur.execute(query)
                return self.cur.fetchall()
        except cx_Oracle.Error as e:
            error_obj, = e.args
            print(f'\nerror is :{error_obj.message}')
            return None

    def commit(self):
        self.con.commit()

    def close(self):
        if self.cur is not None:
            self.cur.close()

    def dismiss(self):
        if self.con is not None:
            self.con.close()

    def statsRecords(self):
        print("Total row affected :", self.stats.getTotalRowAffected())
        print("Total error :", self.stats.getTotalErrorCount())
        print("Total duplicate data :", self.stats.getTotalDuplicationCount())
        print(f"Errors in:\n {[er for er in self.stats.getErrorsRow()]}")
        print("\n")

    def result(self):
        if self.stats.isError:
            print(f'Multiple records of api are not inserted successfully.')
            self.reason = "Database Exception found." if self.stats.getTotalErrorCount() > 0 else "Duplicate data found"
            isSuccessfullyAdd = not self.stats.isError
        else:
            print('Multiple records of api are inserted successfully.')
            isSuccessfullyAdd = not self.stats.isError
            self.reason = ""

        return isSuccessfullyAdd

    def issues(self):
        return self.reason






class Stats:
    issue = ['unique constraint',
             'value larger than specified precision allowed for this column']

    error_count = 0
    dupl_count = 0
    error_rows = []
    isError = False

    def __init__(self, batch_error, dml_row):
        self.batchError = batch_error
        self.dml_row = dml_row
        self.calculate()

    def calculate(self):
        self.error_row = ErrorRow()
        for error in self.batchError:
            if error.message.find(self.issue[0]) > -1:
                self.dupl_count = self.dupl_count + 1
            else:
                self.isError = True
                self.error_count = self.error_count + 1
                self.error_rows.append(self.error_row.getErrorRow(error.offset, error.message, error.code))
                # print("Error", error.message, "at row offset", error.offset)

    def getTotalErrorCount(self):
        return self.error_count

    def getTotalDuplicationCount(self):
        return self.dupl_count

    def getTotalRowAffected(self):
        return len(self.dml_row)

    def getErrorsRow(self):
        return self.error_rows
