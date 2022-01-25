# import pdfplumber
# import pandas as pd
# from xml.etree import ElementTree
# import glob
# import decimal
# import requests
# import json
# import cx_Oracle
# from pdf_app.acc_date_time_value import DateTimeValue
# from pdf_app.db_manager import DBManager
# from dict_aif import dics
# pdf_file = r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Statement from Phi Capital Dt.29.09.2021 of Sanskrut Tradecom Pvt.Ltd..pdf"
# xml_file = r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\AIF_xml\Statement from Phi Capital Dt.29.09.2021 of Sanskrut Tradecom Pvt.Ltd.0.xml"
#
# def xmls():
#     dis = {}
#     dis1 = {}
#     xml_data = glob.glob(xml_file)
#     # print(xml_data)
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
# maped_value_dict = {}
# def main():
#     user = "ACCORD"
#     password = "ACCORD"
#     dsn = "122.166.157.90/IBSorcl"
#     encoding = "UTF-8"
#
#     dbmanager = DBManager(user, password, dsn, encoding)
#
#     dis = xmls()
#     print(dis)
#     pdf = pdfplumber.open(pdf_file)
#     p0 = pdf.pages[1]
#     w1 = p0.width
#     h1 = p0.height
#     # print(w1)
#     for key, value in dis.items():
#         # print(key)
#         # print(value)
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#                 # print(w)
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if "Header" in k:
#                 print("Headers under " + k+" are :-")
#                 # print(k)
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#                 for c, m in (value.items()):
#                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
#                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
#                         stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
#                         print(decimal.Decimal(m[0])*a)
#                         # print(stat)
#                         if stat:
#                             print(c + " : " + stat)
#                             maped_value_dict.update({c: stat})
#
#                         # try:
#                         #     dictn = dic()
#                         #     for K, V in dictn.items():
#                         #         if c == V:
#                         #             cur = con.cursor()
#                         #             sql1 = "UPDATE AIFSTMTMASTER SET (%s)=(%s) where AIF_STATEMENT_TYPE =AlteriaCapitalIndiaFund" %(K,stat)
#                         #             r = cur.execute(sql1)
#                         # except cx_Oracle.DatabaseError as er:
#                         #     print('There is an error in Oracle database 2 **:', er)
#                         # else:
#                         #     con.commit()
#                         #     print('Success')
#                         # finally:
#                         # print("--------------------------------------------------------------------------------------------------")
#
#     # print("----------------------------End Of Pavitra Side Value Display-------------------------------------")
#
#     print("---------------------For saving header--------------------")
#     query, rows = getQuery()
#     if dbmanager is not None:
#         print("-----------------------------------------")
#         print(rows)
#         dbmanager.saveAll(query, [rows])
#         dbmanager.statsRecords()
#
# def getQuery():
#     query = ""
#     val = ""
#     rows = []
#     dat_time_value = DateTimeValue()
#     index = 1
#     # dics_aif = dics()
#     for key, value in maped_value_dict.items():
#         print(key+":"+value)
#         query = query + ',' + key
#         val = val + ',' + f':{index}'
#         index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
#         print("value is : "+value.strip().replace('%', ''))
#         if dat_time_value.isValueTimestamp(value.strip()):
#             dt = dat_time_value.getTimeValue(value)
#             print("Date time is : ",sep='')
#             print(dt)
#             # print(f"Date is : {val}")
#             rows.append(dt)
#         else:
#             # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
#             # rows.append(value.strip().replace('%', ''))
#             rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
#
#         print(val[1:])
#         print("----------------------------------------------------")
#
#     query = f'INSERT INTO AIFSTMTMASTER({query[1:]}) VALUES({val[1:]})'
#     print(query)
#     return query, rows
#
#
# def convertCommaValueIntoNumber(v):
#     num = ""
#     flag = False
#     for i in v.split(','):
#         try:
#             if type(int(i)) is not str:
#                 flag = True
#             if type(float(i)) is not str:
#                 flag = True
#         except:
#             pass
#
#         if flag:
#             num = num + i
#             num.replace(',', '')
#         else:
#             return v
#     try:
#         return float(num)
#     except Exception as e:
#         print(e)
#         return None
# main()
# def table():
#
#     table_count = 1
#     table_json_list = []
#     ##For count table @Edit by Nikunj
#
#     row_item = []
#
#     dis = xmls()
#     # print(dis)
#     pdf = pdfplumber.open(pdf_file)
#     p0 = pdf.pages[0]
#     w1 = p0.width
#     h1 = p0.height
#     # print(w1)
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if f"Transaction_Table{table_count}" == k:
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#                 response_json = {}
#                 for c, m in (value.items()):
#                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
#                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
#                         stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
#                         if stat:
#                             t_row = stat.split('\n')
#                             count = 0
#                             item_dict = {}
#                             row_dict = {}
#                             for r in t_row[1:]:
#                                 item_dict.update({f"{count}": r})
#                                 count = count+1
#                             row_dict.update({c: item_dict})
#                             row_item.append(row_dict)
#                 response_json.update({k: row_item})
#
#                 print("************************************************************")
#                 print(f"Actual Header of Table Response is column wise below :\n {response_json}")
#                 with open(r'D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\Transaction_Table.json', 'w') as f:
#                     json.dump(response_json, f)
#
#                 table_json_list.append(response_json)
#                 table_count +=1 #To Count Table in pdf
#     print("************************************************************")
#     print(f"Actual Header of Table Response is column wise below :\n {table_json_list}")
#     with open(r'D:\nikunj\PycharmProjects\IBSFintech\Accord\pdf_reading\Transaction_Table.json', 'w') as f:
#         json.dump(table_json_list, f)

import pdfplumber
print(pdfplumber.__version__)

pdf = pdfplumber.open(r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Achal Anil Bakeri - HUF 2021Q1_Chiratae_Ventures_India_Fund_IV_Unit_statement_1089 as on 31.03.2021.pdf")

p0 = pdf.pages[0]

im = p0.to_image()
print(im)