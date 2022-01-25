import glob
import os

def document_type():
    files = glob.glob(r'D:\Users\rishi\mail_reading\Mail_Document\*.*')
    for file in files:
        # print(file)
        if file.endswith(".jpg"):
            print(os.path.basename(file))
        elif file.endswith(".xml"):
            print(os.path.basename(file))
        elif file.endswith(".pdf"):
            print(os.path.basename(file))
        elif file.endswith(".xlsx"):
            print(os.path.basename(file))
        elif file.endswith(".png"):
            print(os.path.basename(file))
        elif file.endswith(".txt"):
            print(os.path.basename(file))
        elif file.endswith(".mp4"):
            print(os.path.basename(file))
        elif file.endswith(".zip"):
            print(os.path.basename(file))
