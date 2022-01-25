import decimal

import pdfplumber
import pandas as pd
from xml.etree import ElementTree
import glob
import os
# from .models import Xmldata
# from models import Xmldata
column = []


def xmls():
    dis = {}
    dis1 = {}
    flag= False

    xml_data = glob.glob(r"D:\Users\rishi\WebScrapping\download\crisil_images\Adani_Enterprises_Limited1.xml")
    print(xml_data)
    # xml_data = list(Xmldata.objects.all().values_list('data', flat=True))
    lst1 = []
    count = 1
    for file in xml_data:
        # print(x)
        x = open(file, 'r').read()
        root = ElementTree.XML(x)
        for size in root.findall('size'):
            w = size.find('width').text
            h = size.find('height').text
            lst1.extend((w, h))
            # print(lst1)
            dis1["size"] = lst1.copy()
            lst1.clear()
        for object in root.findall('object'):
            name = object.find('name').text

            if flag:
               column.append(name)

            if name == "Transaction_Table":
                column.append(name)
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

def main():
    dis = xmls()
    # print(dis)
    pdf = pdfplumber.open(r"D:\Users\rishi\WebScrapping\download\Crisil\Adani_Enterprises_Limited.pdf")
    # print(pdf)
    p0 = pdf.pages[1]
    w1 = p0.width
    h1 = p0.height
    print(column)
    for key,value in dis.items():
        for k ,v in sorted (value.items()):
            if k == "size":
                w = int(v[0])
                h = int(v[1])
    a=w1/w
    b=h1/h
    new_list=[]
    new_list1=[]
    count = 0
    for key,value in dis.items():
        # m = None
        # n = None
        for k,v in sorted (value.items()):

            # if flag:
            #     for c, m in (value.items()):
            #         print(f"after trans {k}")
            #         column.append(k)

            if k == "Transaction_Table":
                x0 = int(v[0]) * a
                y0 = int(v[1]) * b
                x1 = int(v[2]) * a
                y1 = int(v[3]) * b
                print(k)

            if k in column:
                new_list.append(int(v[0])*a)
                count = count+1
                m = int(v[0])
                n = int(v[1])
    new1= m*a
    new = n*b
    new_list.append(new1)
    new_list.append(new)
    new_list.sort()
    print(new_list)
    p1 = p0.crop((x0,y0,x1,y1),relative=True)
    w1 = p1.width
    print(w1)
    h1 = p1.height
    print(h1)
    stat = p1.extract_table(table_settings={
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": new_list,
        "explicit_horizontal_lines": new_list,
        "snap_tolerance":5,
        "text_x_tolerance": 10,
        "text_y_tolerance": 10,
        "intersection_x_tolerance": 8,
        "intersection_y_tolerance": 10})
    print(stat)
    # df = pd.DataFrame(stat, column= stat)
    # print(df)
    # df.to_csv(r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\test4.csv")
main()

