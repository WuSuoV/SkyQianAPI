import smtplib
from email.mime.text import MIMEText
from config import myemail


class aemail:

    def __init__(self, receivers: str = myemail.get('receiver')):
        self.receivers = receivers
        self.host = myemail.get('host')
        self.user = myemail.get('user')
        self.password = myemail.get('password')
        self.sender = myemail.get('sender')

    def send(self):
        try:
            asmtp = smtplib.SMTP_SSL(host=self.host, port=465)
            asmtp.login(user=self.user, password=self.password)
            asmtp.sendmail(from_addr=self.sender, to_addrs=self.receivers, msg=self.message.as_string())
            asmtp.quit()
            return 'success'
        except smtplib.SMTPException as e:
            return str(e)

    def set_text(self, text: str):
        self.text = text
        self.message = MIMEText(self.text, 'plain', 'utf-8')
        self.message['subject'] = 'From SkyQianApi'
        self.message['From'] = myemail.get('sender')
        self.message['To'] = self.receivers
