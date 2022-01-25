import pdfplumber
import pandas as pd
from xml.etree import ElementTree
import glob
import decimal
import requests
import json
import cx_Oracle
from dict import dic
def xmls():
    dis = {}
    dis1 = {}
    xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\AIF_xml\Investment statement for the month of Aug-21 of ICICI Real Estate of Achal Anil Bakeri SOA_57000003920.xml")
    # print(xml_data)
    lst1 = []
    count = 1
    for file in xml_data:
        x = open(file, 'r').read()
        root = ElementTree.XML(x)
        for size in root.findall('size'):
            w = size.find('width').text
            h = size.find('height').text
            lst1.extend((w, h,"0","0"))
            # print(lst1)
            dis1["size"] = lst1.copy()
            lst1.clear()
        for object in root.findall('object'):
            name = object.find('name').text
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

def main():
    new_list=[]
    try:
        # con = cx_Oracle.connect("COROTF_DEV/COROTF_DEV@IBSorcl/122.166.157.90")
        con = cx_Oracle.connect(user="ACCORD", password="ACCORD",
                                dsn="122.166.157.90/IBSorcl",
                                encoding="UTF-8")

    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)

    else:
        pass
    try:
        cur = con.cursor()
        sql = fr"INSERT INTO AIFSTMTMASTER (AIF_STATEMENT_TYPE,AIF_STATEMENT_DATE ) VALUES ('Abakkus','12/21/2021')"
        r = cur.execute(sql)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database 2 *:', er)

    # except Exception as er:
    #     print(er)

    else:
        con.commit()
        print('Success')

    dis = xmls()
    print(dis)
    pdf = pdfplumber.open(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Investment statement for the month of Aug-21 of ICICI Real Estate of Achal Anil Bakeri SOA_5700000392.pdf")
    p0 = pdf.pages[0]
    w1 = p0.width
    h1 = p0.height
    # print(w1)
    for key, value in dis.items():
        # print(key)
        # print(value)
        for k, v in (value.items()):
            if k == "size":
                w = int(v[0])
                h = int(v[1])
                # print(w)
    a = w1 / w
    b = h1 / h
    # a = decimal.Decimal(a)
    # b = decimal.Decimal(b)
    for key,value in dis.items():

        for k,v in (value.items()):
            if  "Header" in k:
                print("Headers under "+ k+" are :-")
                # print(k)
                x0 = int(v[0])
                y0 = int(v[1])
                x1 = int(v[2])
                y1 = int(v[3])
                for c,m in (value.items()):
                    if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
                        p1 = p0.crop((decimal.Decimal(m[0])*decimal.Decimal(a), decimal.Decimal(m[1])*decimal.Decimal(b), decimal.Decimal(m[2])*decimal.Decimal(a), decimal.Decimal(m[3])*decimal.Decimal(b)), relative=True)
                        stat = p1.extract_text(x_tolerance=5, y_tolerance=5)
                        print(decimal.Decimal(m[0])*decimal.Decimal(a))
                        # print(stat)
                        if stat:
                            print(c + " : "+ stat)
                        try:
                            dictn = dic()
                            for K,V in dictn.items():
                                if c == V:
                                    cur = con.cursor()
                                    sql = "UPDATE AIFSTMTMASTER (%s)= (%s) where AIF_STATEMENT_TYPE =Abakkus" % (K,stat)
                                    r = cur.execute(sql)
                        except cx_Oracle.DatabaseError as er:
                            print('There is an error in Oracle database 2 **:', er)

                        # except Exception as er:
                        #     print(er)

                        else:
                            con.commit()
                            print('Success')
    # for key, value in dis.items():
    #
    #     for k, v in sorted (value.items()):
    #         if "Transaction_Table" in k:
    #             print("Transaction_Table " + k + " are :-")
    #             # print(k)
    #             x0 = int(v[0])
    #             y0 = int(v[1])
    #             x1 = int(v[2])
    #             y1 = int(v[3])
    #             p1 = p0.crop((decimal.Decimal(x0) * decimal.Decimal(a), decimal.Decimal(y0) * decimal.Decimal(b), decimal.Decimal(x1) * decimal.Decimal(a),
    #                       decimal.Decimal(y1) * decimal.Decimal(b)), relative=True)
    #             for m, n in sorted(value.items()):
    #                 if "Column" in m and int(n[0]) <= x0:
    #                     new_list.append(decimal.Decimal(n[0])* decimal.Decimal(a))
    #                     print(new_list)
    #
    #
    #             stat = p1.extract_table(table_settings={
    #                         "vertical_strategy": "explicit",
    #                         "horizontal_strategy": "lines",
    #                         "explicit_vertical_lines": new_list[0:],
    #                         "explicit_horizontal_lines": new_list[0:-1],
    #                         "snap_tolerance": 8,
    #                         # "join_tolerance": 10,
    #                         # "edge_min_length": 10,
    #                         # "min_words_vertical": 8,
    #                         # "min_words_horizontal":8,
    #                         # "keep_blank_chars": True,
    #                         # "text_tolerance": 10,
    #                         # "text_x_tolerance": 8,
    #                         # "text_y_tolerance": 10,
    #                         # "intersection_tolerance": 10,
    #                         "intersection_x_tolerance": 8,
    #                         "intersection_y_tolerance": 10})
    #             print(stat)
main()
