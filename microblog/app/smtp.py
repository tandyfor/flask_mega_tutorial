import smtplib

from logging.handlers import SMTPHandler


class SSLSMTPHandler(SMTPHandler):
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials = None, secure = None, timeout = 5):
        super().__init__(mailhost, fromaddr, toaddrs, subject, credentials, secure, timeout)
        self.credentials = credentials

    def emit(self, record):
        try:
            port = self.mailport if self.mailport else smtplib.SMTP_SSL_PORT
            with smtplib.SMTP_SSL(self.mailhost, port) as smtp:
                if self.credentials:
                    smtp.login(*self.credentials)
                msg = self.format(record)
                smtp.sendmail(self.fromaddr, self.toaddrs, msg)
        except Exception:
            self.handleError(record)
