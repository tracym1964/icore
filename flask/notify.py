import os, smtplib, socket  # ,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    """
    Send an email notification
    """

    def __init__(self):
        os.environ["NLS_LANG"] = ".AL32UTF8"
        self.hostnm = socket.gethostname().upper()
        self.email_from = "bryan_robinson@eogresources.com"
        self.email_to = []
        self.email_to.append("bryan_robinson@eogresources.com")
        self.email_subject = self.hostnm + " Load_src_data_to_trg2_Failed"

    # create function to send email
    def send_email(self, email_from, email_to, email_subject, email_body):
        if email_from:
            self.email_from = email_from
        if email_to:
            self.email_to = []
            self.email_to.append(email_to)
        if email_subject:
            self.email_subject = email_subject

        msg = MIMEMultipart()
        msg.attach(MIMEText(email_body))
        msg['Subject'] = self.email_subject
        msg['From'] = self.email_from
        msg['To'] = ', '.join(self.email_to)

        try:
            smtp_obj = smtplib.SMTP('smtp.eogresources.com')
            smtp_obj.sendmail(self.email_from, self.email_to, msg.as_string())
            smtp_obj.quit()
        except smtplib.SMTPException as exc:
            error, = exc.args
            error_msg = error.message
        return None
