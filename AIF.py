# import pdfplumber
# from pdf2image import convert_from_path
# import pandas as pd
# from xml.etree import ElementTree
# import glob
# import decimal
# import json
# import requests
# import json
# import cx_Oracle
# # from dict import dic
# from pdf_app.acc_date_time_value import DateTimeValue
# from pdf_app.db_manager import DBManager
#
# path = fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Achal Anil Bakeri - HUF 2021Q1_Chiratae_Ventures_India_Fund_IV_Unit_statement_1089 as on 31.03.2021.pdf"
# #Statement from Alteria Dt.30.06.2020.pdf
# user = "ACCORD"
# password = "ACCORD"
# dsn = "122.166.157.90/IBSorcl"
# encoding = "UTF-8"
#
# dbmanager = DBManager(user, password, dsn, encoding)
# column = []
# def xmls():
#     dis = {}
#     dis1 = {}
#     flag = False
#     xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\AIF_xml\Achal Anil Bakeri - HUF 2021Q1_Chiratae_Ventures_India_Fund_IV_Unit_statement_1089 as on 31.03.20210.xml")
#     #Statement from Alteria Dt.30.06.20200.xml
#     #Statement from Alteria Dt.30.09.20201.xml
#     #Statement from Alteria Dt.31.03.20210.xml
#     #'Error1722: ORA-01722: invalid number at row offset 0']
#     lst1 = []
#     count = 1
#     for file in xml_data:
#         x = open(file, 'r').read()
#         root = ElementTree.XML(x)
#         for size in root.findall('size'):
#             w = size.find('width').text
#             h = size.find('height').text
#             lst1.extend((w, h,"0","0"))
#             # print(lst1)
#             dis1["size"] = lst1.copy()
#             lst1.clear()
#         for object in root.findall('object'):
#             name = object.find('name').text
#             if flag:
#                column.append(name)
#
#             if name == "Transaction_Table":
#                 column.append(name)
#                 flag = True
#             for bndbox in object.findall('bndbox'):
#                 x0 = bndbox.find('xmin').text
#                 y0 = bndbox.find('ymin').text
#                 x1 = bndbox.find('xmax').text
#                 y1 = bndbox.find('ymax').text
#                 lst1.extend((x0, y0, x1, y1))
#                 # print(lst1)
#                 dis1[name] = lst1.copy()
#                 lst1.clear()
#         dis[count] = dis1.copy()
#         dis1.clear()
#         count = count + 1
#     return dis
#
# ##----------------------------------Header Extraction---------------------------------------
# # def header():
# #     row_item = []
# #     response_json = {}
# #
# #     dis = xmls()
# #     print(dis)
# #     pdf = pdfplumber.open(path)
# #     p0 = pdf.pages[0]
# #     w1 = p0.width
# #     h1 = p0.height
# #     # print(w1)
# #     for key, value in dis.items():
# #         for k, v in (value.items()):
# #             if k == "size":
# #                 w = int(v[0])
# #                 h = int(v[1])
# #                 # print(w)
# #     a = w1 / w
# #     b = h1 / h
# #     for key, value in dis.items():
# #
# #         for k, v in (value.items()):
# #             if "Header" in k:
# #
# #                 row_dict = {}
# #
# #                 x0 = int(v[0])
# #                 y0 = int(v[1])
# #                 x1 = int(v[2])
# #                 y1 = int(v[3])
# #                 for c, m in (value.items()):
# #                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
# #                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
# #                         stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
# #                         if stat:
# #                             print(f"Actual value is : {stat}")
# #                             if stat.find('\n') > 0:
# #                                 row_dict.update({c: stat.split('\n')[-1]})
# #                             else:
# #                                 row_dict.update({c: stat})
# #
# #                 row_item.append(row_dict)
# #                 response_json.update({k: row_item})
# #
# #     print("************************************************************")
# #     print(f"Actual Header Response is column wise below :\n {response_json}")
# #     with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json', 'w') as f:
# #         json.dump(response_json, f)
#
#
#
# ##------------------------------------------Query with Single Row Value Creation Method------------------------------
# # def getQuery(maped_value_dict, table_name):
# #     query = ""
# #     val = ""
# #     rows = []
# #     dat_time_value = DateTimeValue()
# #     index = 1
# #     # dics_aif = dics()
# #     for key, value in maped_value_dict.items():
# #         print(key+":"+value)
# #         query = query + ',' + key
# #         val = val + ',' + f':{index}'
# #         index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
# #         print("value is : "+value.strip().replace('%', ''))
# #         print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
# #         if dat_time_value.isValueTimestamp(value.strip()):
# #             dt = dat_time_value.getTimeValue(value)
# #             # print(f"Date is : {val}")
# #             print("Date time is : ", sep='')
# #             print(dt)
# #             rows.append(dt)
# #         else:
# #             # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
# #             # rows.append(value.strip().replace('%', ''))
# #             rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
# #
# #         print(val[1:])
# #         print("----------------------------------------------------")
# #
# #     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
# #     print(query)
# #     return query, rows
#
#
# ##-----------------Save Header Into Database---------------------------------------
# # def saveHeader(path_of_json_file):
# #     with open(path_of_json_file, 'r') as f:
# #         header_data = json.load(f)
# #
# #     print(header_data['Header'][0])
# #     query, rows = getQuery(header_data['Header'][0], 'AIF_HEADER')
# #     if dbmanager is not None:
# #         print("-------------------Save Header----------------------")
# #         print(rows)
# #         dbmanager.saveAll(query, [rows])
# #         dbmanager.statsRecords()
# #         dbmanager.result()
# ##------------------------------------End Header----------------------------------------------
#
# ##----------------------------------------Table Data Extraction-----------------------------------
# def table():
#     row_item = []
#     response_json = {}
#     dis = xmls()
#     # print(dis)
#     pdf = pdfplumber.open(path)
#     p0 = pdf.pages[0]
#     w1 = p0.width
#     h1 = p0.height
#     root_column_name = ""
#     # print(w1)
#     new_list = []
#     count = 0
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "Transaction_Table":
#                 x0 = int(v[0]) * a
#                 y0 = int(v[1]) * b
#                 x1 = int(v[2]) * a
#                 y1 = int(v[3]) * b
#                 print(k)
#                 root_column_name = k
#
#             if k in column:
#                 new_list.append(int(v[0]) * a)
#                 count = count + 1
#                 m = int(v[0])
#                 n = int(v[1])
#
#         new1 = m * a
#         new = n * b
#         new_list.append(new1)
#         new_list.append(new)
#         new_list.sort()
#         # print(new_list)
#         p1 = p0.crop((x0, y0, x1, y1), relative=True)
#         w1 = p1.width
#         # print(w1)
#         h1 = p1.height
#         # print(h1)
#         # stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
#         stat = p1.extract_table(table_settings={
#             "vertical_strategy": "lines",
#             "horizontal_strategy": "lines",
#             "explicit_vertical_lines": new_list,
#             "explicit_horizontal_lines": new_list,
#             "min_words_vertical": 3,
#             "min_words_horizontal": 7,
#             "keep_blank_chars": False,
#             "snap_tolerance": 7,
#             "snap_x_tolerance": 3,
#             "snap_y_tolerance": 3,
#             "text_x_tolerance": 5,
#             "text_y_tolerance": 5,
#             "intersection_x_tolerance": 8,
#             "intersection_y_tolerance": 8
#         })
#
#         # print(type(stat))
#         print(stat)
#         # df = pd.DataFrame(stat, column= stat)
#         # print(df)
#         # df.to_csv(r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\test4.csv")
#         # for item in stat:
#         #     print("-------------------")
#         #     print(item)
#         #     print('\n')
#
#             #To Do
#             #Cleaning Data
#             #1. If we getting completely null row then it should be remove
#             #2. Proper showing if we get any \n value
#             #3. None set
#         # if stat:
#         #     # if stat.'\n'
#         #     t_row = stat.split('\n')
#         #     count = 0
#         #     item_dict = {}
#         #     row_dict = {}
#         #     for r in t_row:
#         #          # for x,y in r.items():
#         #         #     if x == "text":
#         #         #
#         #         #         print(y)
#         #         item_dict.update({f"{count}": r})
#         #         count = count+1
#         #     row_dict.update({k: item_dict})
#         #     row_item.append(row_dict)
#         # response_json.update({k: row_item})
#         # print("************************************************************")
#         # print(f"Actual Header of Table Response is column wise below :\n {response_json}")
#         # with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Transaction_Table.json', 'w') as f:
#         #     json.dump(response_json, f)
#
# ##------------------------------------------Query with Multiple Row Value Creation Method------------------------------
# # def getQueryForAllRow(maped_value_dict, table_name):
# #     query = ""
# #     val = ""
# #     rows = []
# #     dat_time_value = DateTimeValue()
# #     index = 1
# #     tr_dict = {}
# #
# #     for tr in maped_value_dict['Transaction_Table']:
# #
# #         for col, rows in tr.items():
# #             print(col+":"+rows)
# #             query = query + ',' + col
# #             val = val + ',' + f':{index}'
# #             index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
# #             print("value is : "+val.strip().replace('%', ''))
# #             row_count = 0
# #             row_list_on_col = []
# #             for r in rows:
# #                 row_list_on_col.append(r[f'{row_count}'])
# #             print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
# #             if dat_time_value.isValueTimestamp(value.strip()):
# #                 dt = dat_time_value.getTimeValue(value)
# #                 # print(f"Date is : {val}")
# #                 print("Date time is : ", sep='')
# #                 print(dt)
# #                 rows.append(dt)
# #             else:
# #                 # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
# #                 # rows.append(value.strip().replace('%', ''))
# #                 rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
# #
# #             print(val[1:])
# #             print("----------------------------------------------------")
# #
# #     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
# #     print(query)
# #     return query, rows
#
#
# ##-----------------------------Handle if wrong value found in any type numeric value------------------------
# # def convertCommaValueIntoNumber(v):
# #     num = ""
# #     flag = False
# #     for i in v.split(','):
# #         try:
# #             if type(int(i)) is not str:
# #                 flag = True
# #             if type(float(i)) is not str:
# #                 flag = True
# #         except:
# #             pass
# #
# #         if flag:
# #             num = num + i
# #             num.replace(',', '')
# #         else:
# #             return v
# #     try:
# #         return float(num)
# #     except Exception as e:
# #         print(e)
# #         return None
#
# ##-------------------Save Table Into Database--------------------------------------
# # def saveTable(path_of_json_file):
# #     with open(path_of_json_file, 'r') as f:
# #         table_data = json.load(f)
# #
# #
# #         for col, rows in tr:
# #             query = query + ',' + key
# #             tr_dict.update({col: rows[f'{row_count}']})
# #
# #         query, row = getQuery(tr_dict)
# #         row_count += 1
# #
# #
# #
# #     query, rows_arr = getQuery(table_data['Transaction_Table'], 'AIF_STATEMENT')
# #     if dbmanager is not None:
# #         print("-------------------Save Table Data----------------------")
# #         print(rows_arr)
# #         dbmanager.saveAll(query, [rows_arr])
# #         dbmanager.statsRecords()
# #         dbmanager.result()
# ##-------------------------------End table saving --------------------------------
#
#
# ##---------------------------------Execution Environment------------------------
# # header()
# # saveHeader(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json')
# # print("-------------------------------End Header--------------------------------")
#
#
# table()


import pdfplumber
from xml.etree import ElementTree
import glob
import decimal
import requests
import json
import pandas as pd

# from Accord.pdf_reading.ExcelSheet import ExcelSheet
# from Accord.pdf_reading.acc_date_time_value import DateTimeValue
# from Accord.pdf_reading.db_manager import DBManager

pdf_file = r"D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\pdf\pdf\AIF\Investment Statement of AMPLUS Realty Fund-II as on 27.07.2021 of Blubay Technologies Pvt. Ltd..pdf"
xml_file = r"D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\pdf\AIF_xml\Investment Statement of AMPLUS Realty Fund-II as on 27.07.2021 of Blubay Technologies Pvt. Ltd.0.xml"
page_no = 0

user = "ACCORD"
password = "ACCORD"
dsn = "122.166.157.90/IBSorcl"
encoding = "UTF-8"

dbmanager = DBManager(user, password, dsn, encoding)
dat_time_value = DateTimeValue()

path = r"D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_content.xlsx"
excel_sheet = ExcelSheet(path)
column = []

'''
    @xmls method to fetch coordinate from xml or annotation file.
    Find object and its bounding box as bndbox.
    @:param - No parameter required
    @:return - dis - type dict
'''
def xmls():
    dis = {}
    dis1 = {}
    flag = False
    xml_data = glob.glob(xml_file)
    #Statement from Alteria Dt.30.06.20200.xml
    #Statement from Alteria Dt.30.09.20201.xml
    #Statement from Alteria Dt.31.03.20210.xml
    #'Error1722: ORA-01722: invalid number at row offset 0']
    lst1 = []
    count = 1
    for file in xml_data:
        x = open(file, 'r').read()
        root = ElementTree.XML(x)
        for size in root.findall('size'):
            w = size.find('width').text
            h = size.find('height').text
            lst1.extend((w, h, "0", "0"))
            # print(lst1)
            dis1["size"] = lst1.copy()
            lst1.clear()

        for object in root.findall('object'):
            name = object.find('name').text
            if flag:
               column.append(name)

            if name == "Transaction_Table":
                flag = True

            for bndbox in object.findall('bndbox'):
                x0 = bndbox.find('xmin').text
                y0 = bndbox.find('ymin').text
                x1 = bndbox.find('xmax').text
                y1 = bndbox.find('ymax').text
                lst1.extend((x0, y0, x1, y1))
                # print(lst1)
                dis1[name] = lst1.copy()
                lst1.clear()
        dis[count] = dis1.copy()
        dis1.clear()
        count = count + 1
    return dis

##----------------------------------Header Extraction---------------------------------------
def header():
    row_item = []
    response_json = {}

    dis = xmls()
    print(dis)
    pdf = pdfplumber.open(pdf_file)
    p0 = pdf.pages[page_no]
    w1 = p0.width
    h1 = p0.height
    # print(w1)
    for key, value in dis.items():
        for k, v in (value.items()):
            if k == "size":
                w = int(v[0])
                h = int(v[1])
                # print(w)
    a = w1 / w
    b = h1 / h
    for key, value in dis.items():

        for k, v in (value.items()):
            if "Header" in k:
                row_dict = {}

                x0 = int(v[0])
                y0 = int(v[1])
                x1 = int(v[2])
                y1 = int(v[3])
                for c, m in (value.items()):
                    if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
                        p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
                        stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
                        if stat:
                            print(f"Actual value is : {stat}")
                            if stat.find('\n') > 0:
                                row_dict.update({c: stat.split('\n')[-1]})
                            else:
                                row_dict.update({c: stat})

                row_item.append(row_dict)
                response_json.update({k: row_item})

    print("************************************************************")
    print(f"Actual Header Response is column wise below :\n {response_json}")
    with open(r'D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\Header.json', 'w') as f:
        json.dump(response_json, f)



##------------------------------------------Query with Single Row Value Creation Method------------------------------
def getQuery(maped_value_dict, table_name):
    query = ""
    val = ""
    rows = []
    index = 1
    # dics_aif = dics()
    for key, value in maped_value_dict.items():
        print(key+":"+value)
        query = query + ',' + key
        val = val + ',' + f':{index}'
        index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
        print("value is : "+value.strip().replace('%', ''))
        print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
        if dat_time_value.isValueTimestamp(value.strip()):
            dt = dat_time_value.getTimeValue(value)
            # print(f"Date is : {val}")
            print("Date time is : ", sep='')
            print(dt)
            rows.append(dt)
        else:
            # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
            # rows.append(value.strip().replace('%', ''))
            rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))

        print(val[1:])
        print("----------------------------------------------------")

    query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
    print(query)
    return query, rows


##-----------------Save Header Into Database---------------------------------------
def saveHeader(path_of_json_file):
    with open(path_of_json_file, 'r') as f:
        header_data = json.load(f)

    print(header_data['Header'][0])
    query, rows = getQuery(header_data['Header'][0], 'AIF_HEADER')
    saveIntoDb(query, [rows])
    # if dbmanager is not None:
    #     print("-------------------Save Header----------------------")
    #     print(rows)
    #     dbmanager.saveAll(query, [rows])
    #     dbmanager.statsRecords()
    #     dbmanager.result()
##------------------------------------End Header----------------------------------------------


##----------------------------------------Table Data Extraction-----------------------------------
table_json_path = r'D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\Transaction_Table.json'
m = None
n = None
stat_list = []
def table():
    stat = []
    dis = xmls()
    pdf = pdfplumber.open(pdf_file)
    p0 = pdf.pages[page_no]
    w1 = p0.width
    h1 = p0.height
    root_column_name = ""
    new_list = []
    count = 0
    for key, value in dis.items():
        for k, v in (value.items()):
            if k == "size":
                w = int(v[0])
                h = int(v[1])
                a = w1 / w
                b = h1 / h

            if k == "Transaction_Table":
                x0 = int(v[0]) * a
                y0 = int(v[1]) * b
                x1 = int(v[2]) * a
                y1 = int(v[3]) * b
                root_column_name = k

            if k in column:
                # print(v[0])
                # new_list.append(int(v[0]) * a)
                count = count + 1
                m = int(v[0])
                n = int(v[1])
                new_list.append(m * a)
                new_list.append(n * a)
                break

        #Outer loop
        new_list.sort()
        p1 = p0.crop((x0, y0, x1, y1), relative=True)

        stat = p1.extract_table(table_settings={
            # "vertical_strategy": "lines",
            "horizontal_strategy": "lines",
            # "explicit_vertical_lines": new_list,
            "explicit_horizontal_lines": new_list,
            # "min_words_vertical": 3,
            # "min_words_horizontal": 2,
            # "keep_blank_chars": True,
            "snap_tolerance": 3,
            # "snap_x_tolerance": 3,
            # "snap_y_tolerance": 3,
            "text_x_tolerance": 3,
            "text_y_tolerance": 3,
            # "intersection_x_tolerance": 8,
            # "intersection_y_tolerance": 8
        })
        break

    response_json = parseJson(stat, column, root_column_name)
    # To Do
    # Cleaning Data
    # 1. If we getting completely null row then it should be remove
    # 2. Proper showing if we get any \n value
    # 3. None set

    print("************************************************************")
    print(f"Actual Header of Table Response is column wise below :\n {response_json}")
    with open(table_json_path, 'w') as f:
        json.dump(response_json, f)

##------------------------------------------Query with Multiple Row Value Creation Method------------------------------
def getQueryRowsForStaging(maped_value_dict, table_name):
    query = ""
    val = ""
    index = 1
    col_list = []
    row_list = []
    jt = pd.DataFrame(maped_value_dict)
    j = json.loads(jt['Transaction_Table'].to_json())
    j = pd.DataFrame(j)
    maped_value_dict = json.loads(j.to_json())
    # Prepare query
    query_count = 0
    for tr, tv in maped_value_dict.items():
        rows = []
        for col, value in tv.items():
            if query_count == 0:
                col_list.append(col)
                query = query + ',' + col
                val = val + ',' + f':{index}'
                index = index + 1

            if dat_time_value.isValueTimestamp(value.strip()):
                dt = dat_time_value.getTimeValue(value)
                rows.append(dt)
            elif value == ' ':
                rows.append(' ')
            else:
                rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))

        query_count += 1
        row_list.append(rows)

        # print(row_list)

    query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
    # print(query)

    return query, row_list


##-------------------Save Table Into Database--------------------------------------
def saveTable():
    with open(table_json_path, 'r') as f:
        table_data = json.load(f)

    query, row_ = getQueryRowsForStaging(table_data, 'AIF_STATMENT')
    print(query)
    print(row_)
    saveIntoDb(query, row_)

##---------------------------------------------------------------------------------------------------------------------

key_list = []
def fetchAllDataFromDataSource(dbmanager):
    """
    Create excel of headers with value where these headers title getting from table called AIFSTMTMASTER
    :param dbmanager: DBManager object
    """
    sheet_name = []
    datas = []
    header_datas = dbmanager.fetchAll("SELECT column_name FROM USER_TAB_COLUMNS WHERE table_name = \'AIFSTMTMASTER\'")
    if header_datas is not None:
        count_header = 0
        for header in header_datas:
            key_list.append(header[0])
            count_header += 1
            print(f"{count_header}. header is : {header[0]}")

    value_datas = dbmanager.fetchAll("SELECT * FROM AIFSTMTMASTER")
    if value_datas is not None:
        for data in value_datas:
            datas.append(list(data))
            sheet_name.append(data[0])
            print(f"sheet name is : {sheet_name}")

    # print(f"Datas is {datas} \n")
    for i in range(len(sheet_name)):
        createExcel(datas[i], sheet_name[i])

    commitExcel()


def createExcel(rows, name_for_sheet):
    print(f"keys item is {len(key_list)} \n")
    print(f"Rows item is {len(rows)} \n")
    print(f"Name is {len(name_for_sheet)} \n")

    excel_sheet.createColumnWiseDict(key_list, [rows], name_for_sheet)


def commitExcel():
    print("Please wait...")
    excel_sheet.createExcel()
    print("Save to excel")
    # self.excel_sheet.resetExcel()


def convertCommaValueIntoNumber(v):
    num = ""

    flag = False
    for i in v.replace(' ', '').split(','):
        try:
            if i != ' ':
                if type(int(i)) is not str:
                    flag = True
                if type(float(i)) is not str:
                    flag = True
        except:
            pass

        if flag:
            num = num + i
            num.replace(',', '')
        else:
            return v
    try:
        return float(num)
    except Exception as e:
        print(e)
        return None

##---------------------------------------------------------------------------
def saveIntoDb(query, rows):
    if dbmanager is not None:
        print("-------------------Save Table----------------------")
        dbmanager.saveAll(query, rows)
        dbmanager.statsRecords()
        dbmanager.result()


##_______________________________To Parse Into Json_____________________
'''
    @parseJson to parse list of row and column into json using pandas dataframe
    where data also refresh
    Parameters
    ----------
        data : list of row list
        col : list of column
        json_name : string name of json
    return
    -------
        json type response
'''
def parseJson(data, col, json_name):
    df = pd.DataFrame(data=data, columns=col)
    df = cleaningData(df)
    df = df.replace('NaN', " ")
    df = df.reset_index(drop=True) #Re indexing after remove row
    df = df.T #Transpose rows
    return {json_name: json.loads(df.to_json())}

def cleaningData(df):
    df = df[1:]#Remove header
    df = df.replace("", 'NaN')
    #Remove empty row
    empty_field_count = 0
    for p in range(len(df)):
        for v in list(df[p:p + 1:].values.tolist()[0]):
            if v == 'NaN':
                empty_field_count += 1
            else:
                break

        if empty_field_count == len(column):
            dq = pd.DataFrame(df[p + 1::])
        empty_field_count = 0
    return dq

##---------------------------------Execution Block------------------------
# header()
# saveHeader(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json')
print("-------------------------------End Header--------------------------------")

table()
saveTable()