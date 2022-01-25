#
# import pdfplumber
# from pdf2image import convert_from_path
# import pandas as pd
# from xml.etree import ElementTree
# import glob
# import decimal
# import requests
# import json
# import cx_Oracle
# from dict import dic
# def xmls():
#     dis = {}
#     dis1 = {}
#     xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\AIF_xml\Statement from Alteria Dt.30.09.20200.xml")
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
#
# def main():
#     # new_list=[]
#     res_dict = {}
#     item_dict = {}
#     row_item = []
#     count = 0
#
#     dis = xmls()
#     print(dis)
#     pdf = pdfplumber.open(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Statement from Alteria Dt.30.09.2020.pdf")
#     p0 = pdf.pages[0]
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
#     for key,value in dis.items():
#
#         for k,v in (value.items()):
#             if  "Transaction_Table" in k:
#                 print(k+" are :-")
#                 # print(k)
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#
#                 for c,m in (value.items()):
#                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
#                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
#                         stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
#                         print(decimal.Decimal(m[0])*a)
#                         # print(stat)
#                         # if count > 0:
#                         #     item_dict.update({count:stat})
#                         #     row_item.append(item_dict)
#                         # count=count+1
#
#                         if stat:
#                             print(c + " : "+ stat)
#                         #
#                         #     print("Key is : " + c)
#                         # print('Success')
#
#                 # print("----------------")
#                 # print(row_item)
#                 # print("------------------")
#
#                 # print(stat)
#
#
#
# main()




#####################
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
# path = fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Investment Statement of BPEA of Sanskrut Tradecom Pvt. Ltd. as on 31.08.2021.pdf"
# #Statement from Alteria Dt.30.06.2020.pdf
# user = "ACCORD"
# password = "ACCORD"
# dsn = "122.166.157.90/IBSorcl"
# encoding = "UTF-8"
#
# dbmanager = DBManager(user, password, dsn, encoding)
#
# def xmls():
#     dis = {}
#     dis1 = {}
#     xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\AIF_xml\Investment Statement of BPEA of Sanskrut Tradecom Pvt. Ltd. as on 31.08.20210.xml")
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
# def header():
#     row_item = []
#     response_json = {}
#
#     dis = xmls()
#     print(dis)
#     pdf = pdfplumber.open(path)
#     p0 = pdf.pages[0]
#     w1 = p0.width
#     h1 = p0.height
#     # print(w1)
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#                 # print(w)
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#
#         for k, v in (value.items()):
#             if "Header" in k:
#
#                 row_dict = {}
#
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#                 for c, m in (value.items()):
#                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
#                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
#                         stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
#                         if stat:
#                             print(f"Actual value is : {stat}")
#                             if stat.find('\n') > 0:
#                                 row_dict.update({c: stat.split('\n')[-1]})
#                             else:
#                                 row_dict.update({c: stat})
#
#                 row_item.append(row_dict)
#                 response_json.update({k: row_item})
#
#     print("************************************************************")
#     print(f"Actual Header Response is column wise below :\n {response_json}")
#     with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json', 'w') as f:
#         json.dump(response_json, f)
#
#
#
# ##------------------------------------------Query with Single Row Value Creation Method------------------------------
# def getQuery(maped_value_dict, table_name):
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
#         print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
#         if dat_time_value.isValueTimestamp(value.strip()):
#             dt = dat_time_value.getTimeValue(value)
#             # print(f"Date is : {val}")
#             print("Date time is : ", sep='')
#             print(dt)
#             rows.append(dt)
#         else:
#             # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
#             # rows.append(value.strip().replace('%', ''))
#             rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
#
#         print(val[1:])
#         print("----------------------------------------------------")
#
#     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
#     print(query)
#     return query, rows
#
#
# ##-----------------Save Header Into Database---------------------------------------
# def saveHeader(path_of_json_file):
#     with open(path_of_json_file, 'r') as f:
#         header_data = json.load(f)
#
#     print(header_data['Header'][0])
#     query, rows = getQuery(header_data['Header'][0], 'AIF_HEADER')
#     if dbmanager is not None:
#         print("-------------------Save Header----------------------")
#         print(rows)
#         dbmanager.saveAll(query, [rows])
#         dbmanager.statsRecords()
#         dbmanager.result()
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
#     # print(w1)
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if "Transaction_Table1" in k:
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#
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
#                 with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Transaction_Table.json', 'w') as f:
#                     json.dump(response_json, f)
    #             if "Transaction_Table2" in k:
    #                 x0 = int(v[0])
    #                 y0 = int(v[1])
    #                 x1 = int(v[2])
    #                 y1 = int(v[3])
    #
    #                 for c, m in (value.items()):
    #                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
    #                         p1 = p0.crop((decimal.Decimal(m[0]) * a, decimal.Decimal(m[1]) * b,
    #                                       decimal.Decimal(m[2]) * a, decimal.Decimal(m[3]) * b), relative=True)
    #                         stat = p1.extract_text(x_tolerance=5, y_tolerance=5)
    #                         if stat:
    #                             t_row = stat.split('\n')
    #                             count = 0
    #                             item_dict = {}
    #                             row_dict = {}
    #                             for r in t_row[1:]:
    #                                 item_dict.update({f"{count}": r})
    #                                 count = count + 1
    #                             row_dict.update({c: item_dict})
    #                             row_item.append(row_dict)
    #                 response_json.update({k: row_item})
    #
    # print("************************************************************")
    # print(f"Actual Header of Table Response is column wise below :\n {response_json}")
    # with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Transaction_Table.json', 'w') as f:
    #     json.dump(response_json, f)

##------------------------------------------Query with Multiple Row Value Creation Method------------------------------
# def getQueryForAllRow(maped_value_dict, table_name):
#     query = ""
#     val = ""
#     rows = []
#     dat_time_value = DateTimeValue()
#     index = 1
#     tr_dict = {}
#
#     for tr in maped_value_dict['Transaction_Table']:
#
#         for col, rows in tr.items():
#             print(col+":"+rows)
#             query = query + ',' + col
#             val = val + ',' + f':{index}'
#             index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
#             print("value is : "+val.strip().replace('%', ''))
#             row_count = 0
#             row_list_on_col = []
#             for r in rows:
#                 row_list_on_col.append(r[f'{row_count}'])
#             print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
#             if dat_time_value.isValueTimestamp(value.strip()):
#                 dt = dat_time_value.getTimeValue(value)
#                 # print(f"Date is : {val}")
#                 print("Date time is : ", sep='')
#                 print(dt)
#                 rows.append(dt)
#             else:
#                 # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
#                 # rows.append(value.strip().replace('%', ''))
#                 rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
#
#             print(val[1:])
#             print("----------------------------------------------------")
#
#     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
#     print(query)
#     return query, rows


##-----------------------------Handle if wrong value found in any type numeric value------------------------
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

##-------------------Save Table Into Database--------------------------------------
# def saveTable(path_of_json_file):
#     with open(path_of_json_file, 'r') as f:
#         table_data = json.load(f)
#
#
#         for col, rows in tr:
#             query = query + ',' + key
#             tr_dict.update({col: rows[f'{row_count}']})
#
#         query, row = getQuery(tr_dict)
#         row_count += 1
#
#
#
#     query, rows_arr = getQuery(table_data['Transaction_Table'], 'AIF_STATEMENT')
#     if dbmanager is not None:
#         print("-------------------Save Table Data----------------------")
#         print(rows_arr)
#         dbmanager.saveAll(query, [rows_arr])
#         dbmanager.statsRecords()
#         dbmanager.result()
##-------------------------------End table saving --------------------------------


##---------------------------------Execution Environment------------------------
# header()
# saveHeader(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json')
# print("-------------------------------End Header--------------------------------")
#
#
# table()





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>new code>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



import pdfplumber
from pdf2image import convert_from_path
import pandas as pd
from xml.etree import ElementTree
import glob
import decimal
import json
import requests
import json
import cx_Oracle
# from dict import dic
from pdf_app.acc_date_time_value import DateTimeValue
from pdf_app.db_manager import DBManager

path = fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\cams\image\CAMS Statement_Symphony.pdf"
#Statement from Alteria Dt.30.06.2020.pdf
user = "ACCORD"
password = "ACCORD"
dsn = "122.166.157.90/IBSorcl"
encoding = "UTF-8"

dbmanager = DBManager(user, password, dsn, encoding)

def xmls():
    dis = {}
    dis1 = {}
    xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\cams\image\CAMS Statement_Symphony0.xml")
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

##----------------------------------Header Extraction---------------------------------------
def header():
    row_item = []
    response_json = {}

    dis = xmls()
    print(dis)
    pdf = pdfplumber.open(path)
    p0 = pdf.pages[0]
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
    with open(r'D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\cams\Header.json', 'w') as f:
        json.dump(response_json, f)



##------------------------------------------Query with Single Row Value Creation Method------------------------------
# def getQuery(maped_value_dict, table_name):
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
#         print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
#         if dat_time_value.isValueTimestamp(value.strip()):
#             dt = dat_time_value.getTimeValue(value)
#             # print(f"Date is : {val}")
#             print("Date time is : ", sep='')
#             print(dt)
#             rows.append(dt)
#         else:
#             # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
#             # rows.append(value.strip().replace('%', ''))
#             rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
#
#         print(val[1:])
#         print("----------------------------------------------------")
#
#     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
#     print(query)
#     return query, rows


##-----------------Save Header Into Database---------------------------------------
# def saveHeader(path_of_json_file):
#     with open(path_of_json_file, 'r') as f:
#         header_data = json.load(f)
#
#     print(header_data['Header'][0])
#     query, rows = getQuery(header_data['Header'][0], 'AIF_HEADER')
#     if dbmanager is not None:
#         print("-------------------Save Header----------------------")
#         print(rows)
#         dbmanager.saveAll(query, [rows])
#         dbmanager.statsRecords()
#         dbmanager.result()
##------------------------------------End Header----------------------------------------------

##----------------------------------------Table Data Extraction-----------------------------------
# def table():
#     row_item = []
#     response_json = {}
#     dis = xmls()
#     # print(dis)
#     pdf = pdfplumber.open(path)
#     p0 = pdf.pages[0]
#     w1 = p0.width
#     h1 = p0.height
#     # print(w1)
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if k == "size":
#                 w = int(v[0])
#                 h = int(v[1])
#     a = w1 / w
#     b = h1 / h
#     for key, value in dis.items():
#         for k, v in (value.items()):
#             if "Transaction_Table" in k:
#                 x0 = int(v[0])
#                 y0 = int(v[1])
#                 x1 = int(v[2])
#                 y1 = int(v[3])
#
#                 for c, m in (value.items()):
#                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
#                         p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
#                         # rows = p1.extract_text().split('\n')
#                         # print(rows)
#                         # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#                         # stat = p1.extract_text(x_tolerance=3, y_tolerance=3)  #, keep_blank_chars=True, use_text_flow=True, horizontal_ltr=True
#                         # print(c+": ", stat)
#                         table_settings = {"vertical_strategy": "lines","horizontal_strategy": "text","explicit_vertical_lines": row_item,"explicit_horizontal_lines": row_item,"snap_tolerance": 8,"intersection_x_tolerance": 10,"intersection_y_tolerance": 10}
#                         stat = p1.extract_table(table_settings)
#                         # df = pd.DataFrame(stat)
#                         # print(df)
#                         # df.to_csv(r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\test4.csv")
#                         # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#                         if stat:
#                             # t_row = stat.split('\n')
#                             count = 0
#                             item_dict = {}
#                             row_dict = {}
#                             for r in stat:
#                                  # for x,y in r.items():
#                                 #     if x == "text":
#                                 #
#                                 #         print(y)
#                                 item_dict.update({f"{count}": r})
#                                 count = count+1
#                             row_dict.update({c: item_dict})
#                             row_item.append(row_dict)
#                 response_json.update({k: row_item})
#
#
#                 print("************************************************************")
#                 print(f"Actual Header of Table Response is column wise below :\n {response_json}")
#                 with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Transaction_Table.json', 'w') as f:
#                     json.dump(response_json, f)
    #             if "Transaction_Table2" in k:
    #                 x0 = int(v[0])
    #                 y0 = int(v[1])
    #                 x1 = int(v[2])
    #                 y1 = int(v[3])
    #
    #                 for c, m in (value.items()):
    #                     if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
    #                         p1 = p0.crop((decimal.Decimal(m[0]) * a, decimal.Decimal(m[1]) * b,
    #                                       decimal.Decimal(m[2]) * a, decimal.Decimal(m[3]) * b), relative=True)
    #                         stat = p1.extract_text(x_tolerance=5, y_tolerance=5)
    #                         if stat:
    #                             t_row = stat.split('\n')
    #                             count = 0
    #                             item_dict = {}
    #                             row_dict = {}
    #                             for r in t_row[1:]:
    #                                 item_dict.update({f"{count}": r})
    #                                 count = count + 1
    #                             row_dict.update({c: item_dict})
    #                             row_item.append(row_dict)
    #                 response_json.update({k: row_item})
    #
    # print("************************************************************")
    # print(f"Actual Header of Table Response is column wise below :\n {response_json}")
    # with open(r'D:\Users\rishi\Table_Extraction\pdf_app\Transaction_Table.json', 'w') as f:
    #     json.dump(response_json, f)

##------------------------------------------Query with Multiple Row Value Creation Method------------------------------
# def getQueryForAllRow(maped_value_dict, table_name):
#     query = ""
#     val = ""
#     rows = []
#     dat_time_value = DateTimeValue()
#     index = 1
#     tr_dict = {}
#
#     for tr in maped_value_dict['Transaction_Table']:
#
#         for col, rows in tr.items():
#             print(col+":"+rows)
#             query = query + ',' + col
#             val = val + ',' + f':{index}'
#             index = index + 1        #str([k for k, v in dics_aif.items() if v == key])
#             print("value is : "+val.strip().replace('%', ''))
#             row_count = 0
#             row_list_on_col = []
#             for r in rows:
#                 row_list_on_col.append(r[f'{row_count}'])
#             print(f" is Date : {dat_time_value.isValueTimestamp(value.strip())}")
#             if dat_time_value.isValueTimestamp(value.strip()):
#                 dt = dat_time_value.getTimeValue(value)
#                 # print(f"Date is : {val}")
#                 print("Date time is : ", sep='')
#                 print(dt)
#                 rows.append(dt)
#             else:
#                 # val = val + ',' + '\'' + value.strip().replace('%', '') + '\''
#                 # rows.append(value.strip().replace('%', ''))
#                 rows.append(convertCommaValueIntoNumber(value.strip().replace('%', '').replace(':', '')))
#
#             print(val[1:])
#             print("----------------------------------------------------")
#
#     query = f'INSERT INTO {table_name}({query[1:]}) VALUES({val[1:]})'
#     print(query)
#     return query, rows


##-----------------------------Handle if wrong value found in any type numeric value------------------------
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

##-------------------Save Table Into Database--------------------------------------
# def saveTable(path_of_json_file):
#     with open(path_of_json_file, 'r') as f:
#         table_data = json.load(f)
#
#
#         for col, rows in tr:
#             query = query + ',' + key
#             tr_dict.update({col: rows[f'{row_count}']})
#
#         query, row = getQuery(tr_dict)
#         row_count += 1
#
#
#
#     query, rows_arr = getQuery(table_data['Transaction_Table'], 'AIF_STATEMENT')
#     if dbmanager is not None:
#         print("-------------------Save Table Data----------------------")
#         print(rows_arr)
#         dbmanager.saveAll(query, [rows_arr])
#         dbmanager.statsRecords()
#         dbmanager.result()
##-------------------------------End table saving --------------------------------


##---------------------------------Execution Environment------------------------
# header()
# saveHeader(r'D:\Users\rishi\Table_Extraction\pdf_app\Header.json')
# print("-------------------------------End Header--------------------------------")


# table()

