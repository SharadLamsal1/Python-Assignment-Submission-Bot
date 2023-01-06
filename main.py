import smtplib
from email.message import EmailMessage
import ssl

assignmentNumber = input('Enter the assignment number: ')

# ENTER SENDER EMAIL AND PASSWORD
yourEmail = 'sender@gmail.com'
yourPw = 'yourgeneratedpassword'
yourName='abc xyz'
yourRollNo=1111
# Note: You should generate new app password from google account

# ENTER RECEIVER EMAIL
receiver = 'receivermail@gmail.com'

# ENTER EMAIL SUBJECT, SENDER NAME AND RECEIVER EMAIL
msg = EmailMessage()
msg['Subject'] = (
    f"Assignment {assignmentNumber} | {yourName} | Roll : {yourRollNo}")
msg['From'] = yourName
msg['To'] = receiver

# READ MAIL BODY FROM TEXT FILE
with open('emailTemplate.txt') as myfile:
    data = myfile.read()
    msg.set_content(data)

# READ THE FILE TO BE ATTACHED AND ATTACH IT TO THE MESSAGE
with open("Assignment.pdf", "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application",
                       subtype="pdf", filename=f.name)


# INITIALIZE SMTP CONNECTION

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(yourEmail, yourPw)  # LOGIN
    server.sendmail(yourEmail, receiver, msg.as_string())  # SEND THE EMAIL

# CONFIRMATION MESSAGE
print('Mail successfully sent !')
