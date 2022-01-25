import imaplib
import base64
import os
import email
import smtplib, ssl
from .document import document_type
from email import utils
from .Document_Type import doc
import re
import mimetypes

def Mail_Reading(Email, Password,Server,Port,Date,doctype,fromemail,subject):
    dis = {}
    counter = 1
    email_user = Email
    email_pass = Password
    mail_server = Server
    port = Port
    mail = imaplib.IMAP4_SSL(mail_server, port)
    mail.login(email_user, email_pass)
    mail.select()
    if fromemail == "ALL" and subject =="ALL":
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids. split()
    elif fromemail != "ALL" and subject =="ALL":
        type, data = mail.search(None, f'(FROM {fromemail})')
        mail_ids = data[0]
        id_list = mail_ids. split()
    elif fromemail == "ALL" and subject != "ALL":
        type, data = mail.search(None, f'(SUBJECT {subject})')
        mail_ids = data[0]
        id_list = mail_ids. split()
    else:
        type, data = mail.search(None, f'(FROM {fromemail} SUBJECT {subject})')
        mail_ids = data[0]
        id_list = mail_ids.split()

    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        raw = email.message_from_bytes(data[0][1])
        datestring = raw['date']
        datestr=str(datestring)
        reg = re.search("\d{2}[ ]\w{3}[ ]\d{4}", datestr)
        if reg:
            print(reg[0])
            print(Date)
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            print(fileName)
            print("#####################################################")
            if bool(fileName):
                res = mimetypes.MimeTypes().guess_type(fileName)
                print(res)
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                result = -1
                if res[0]:
                    result = res[0].find(doctype)
                if result != -1 or doctype == "empty":
                    if Date =="empty":
                        filePath = os.path.join(f'D:\\Users\\rishi\\Mail_Reader\\Mail_Documents\\Documents', fileName)

                        if not os.path.isfile(filePath):
                            fp = open(filePath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            dis[counter]=fileName
                            counter= counter +1
                            fp.close()
                    elif Date:
                        if os.path.isdir(f'D:\\Users\\rishi\\Mail_Reader\\Mail_Documents\\{Date}'):
                            pass
                        else:
                            os.mkdir(os.path.join(f'D:\\Users\\rishi\\Mail_Reader\\Mail_Documents\\',Date))
                        filePath = os.path.join(f'D:\\Users\\rishi\\Mail_Reader\\Mail_Documents\\{Date}', fileName)

                        if not os.path.isfile(filePath) :
                            if reg:
                                if Date == reg[0]:
                                    fp = open(filePath, 'wb')
                                    fp.write(part.get_payload(decode=True))
                                    dis[counter] = fileName
                                    counter = counter + 1
                                    fp.close()
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_from = msg['from']
                email_to =  msg["to"]
                email_subject = msg['subject']
                print('From : ' + email_from + '\n')
                print('to : ' + email_to + '\n')
                print('Subject : ' + email_subject + '\n')
    return dis
