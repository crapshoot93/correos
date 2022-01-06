import smtplib
import chevron
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(recipient):
    # create message object instance
    msg = MIMEMultipart()
    
    message = "Hola {{CLIENT_NAME}}, hoy es {{DATE}}."

    variables = {
        "CLIENT_NAME": "Mauro",
        "DATE": "hoy mismo"
    }

    mail_body = chevron.render(message, variables)
    
    # setup the parameters of the message
    password = "MaNsPa2021"
    msg['From'] = "mantenimientos@nsolar.net"
    msg['To'] = recipient
    msg['Subject'] = "Prueba desde vs-code y python"
    
    # add in the message body
    msg.attach(MIMEText(mail_body, 'plain'))

    # attach files
    filename_to_attach = "./documents/tigo.txt"
    file_to_attach = MIMEApplication(open(filename_to_attach, 'rb').read())
    file_to_attach.add_header('Content-Disposition', 'attachment', filename= 'tigo.txt')
    msg.attach(file_to_attach)
    
    #create server
    server = smtplib.SMTP('secure.emailsrvr.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print ("Successfully sent email to %s:" % (msg['To']))