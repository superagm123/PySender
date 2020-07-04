import smtplib
from email.message import EmailMessage


class Email:
    _host = 'smtp.gmail.com'
    _port = 587
    _email = 'your email here!'
    _password = 'your password here!'

    def __init__(self):
        self.message = EmailMessage()

    def compose_email(self, from_, to, subject, content):
        self.message['from'] = from_
        self.message['to'] = to
        self.message['subject'] = subject
        self.message.set_content(content)

    def send_email(self):
        with smtplib.SMTP(host=self._host, port=self._port) as smtp:
            smtp.starttls()
            smtp.login(self._email, self._password)
            smtp.send_message(self.message)