import pdfplumber
from pdf2image import convert_from_path
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
    xml_data = glob.glob(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\crisil_xml\Adani_Enterprises_Limited1.xml")
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
    dis = xmls()
    print(dis)
    pdf = pdfplumber.open(fr"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\crisil\Adani_Enterprises_Limited.pdf")
    p0 = pdf.pages[1]
    w1 = p0.width
    h1 = p0.height
    for key, value in dis.items():
        for k, v in (value.items()):
            if k == "size":
                w = int(v[0])
                h = int(v[1])
    a = w1 / w
    b = h1 / h
    for key,value in dis.items():

        for k,v in (value.items()):
            if  "MLD_Valuations_06_jan_2022" in k:
                print(k+" are :-")
                # print(k)
                x0 = int(v[0])
                y0 = int(v[1])
                x1 = int(v[2])
                y1 = int(v[3])

                for c,m in (value.items()):
                    if int(m[0]) > x0 and int(m[1]) > y0 and int(m[2]) < x1 and int(m[3]) < y1 and c != "size":
                        p1 = p0.crop((decimal.Decimal(m[0])*a, decimal.Decimal(m[1])*b, decimal.Decimal(m[2])*a, decimal.Decimal(m[3])*b), relative=True)
                        stat = p1.extract_text(x_tolerance=3, y_tolerance=3)
                        print(decimal.Decimal(m[0])*a)

                        if stat:
                            print(c + " : "+ stat)

main()
