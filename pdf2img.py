import os
from pdf2image import convert_from_path
import os
def pdf_jpg(Name):
    pdfs = fr"D:\Users\rishi\WebScrapping\download\mld_valuation crisil\{Name}.pdf"

    pages = convert_from_path(pdfs, 500, poppler_path=r'D:\Users\rishi\WebScrapping\poppler-0.68.0_x86\poppler-0.68.0\bin')
    os.chdir(r"D:\Users\rishi\WebScrapping\download\crisil_images")
    # output = r"D:\Users\rishi\regex-pdf\jpg"
    # res = os.walk(output)
    i = 0
    for page in pages:
        image_name = Name+str(i)+".jpg"
        page.save(image_name, "JPEG")
        # break
        i = i+1
pdf_jpg("Vivriti_Capital_Private_Limited")