import os
import win32com.client as win32
def sender():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = '781038@cognizant.com'
    mail.Subject = 'Test Mail'
    mail.Body = 'Test Mail'
    mail.HTMLBody = '<h2>Hi Sahithi</h2>' #this field is optional

    path=os.getcwd()
#To attach a file to the email (optional):
    attachment=path+"\\report.zip"
    mail.Attachments.Add(attachment)

    mail.Send()
    print("Mail Sent")
