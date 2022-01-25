import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = "D:\\Users\\rishi\\Table_Extraction\\pdf_app\\pdf\\AIF_xml\\"


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

    tree = ET.parse(file)
    root = tree.getroot()
    for elt in tree.iter():
        # if elt.tag == 'name' and elt.text == 'Top_Right':
        if elt.tag == 'name' and elt.text == 'Column1':
            elt.text = 'AIF_Tran_Date'
            # print(elt.text)


    tree.write(file)
    # print(file)


# import pdfplumber
# import pandas as pd
# pdf = pdfplumber.open(r"D:\Users\rishi\Table_Extraction\pdf_app\pdf\pdf\AIF\Abakkus Statement 31.08.2021.pdf")
# print(pdf)
# # p0 = pdf.pages[0]
# p1 = pdf.pages[0]
# table = p1.extract_table(table_settings={"vertical_strategy": "explicit",
#                                          "horizontal_strategy": "text",
#                                          "explicit_vertical_lines": [0],
#                                          "snap_tolerance": 5,})
# df = pd.DataFrame(table, columns=table[0])
# print(df)

