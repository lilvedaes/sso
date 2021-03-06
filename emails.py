import smtplib
from os import environ
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail_helper(r, server, send_from, to):

    body =\
    """
    <html>
        <body>
            <p>
                {} has sent you a message:
            </p>
            <ul>
                <label>Data:</label>
                <li>Email: {}</li>
                <li>Phone: {}</li>
            <ul>
            <p>
            Message: {}
            </p>
        </body>
    </html>
    """.format(r["name"],
               r["email"],
               r["phone"],
               r["body"]
        )

    mail = MIMEMultipart()
    mail["From"] = send_from
    mail["Subject"] = "Website message"

    mail["To"] = to
    mail.attach(MIMEText(body, 'html'))

    server.sendmail(
      send_from,  # from
      to,               # to
      mail.as_string()) # body


def send_mail(r):
    send_to = "Spanishorganizationutsc@gmail.com"
    server_username = "Spanishorganizationutsc@gmail.com"
    server_password = environ.get('SSO_MAIL_PASS')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_username, server_password)

    send_mail_helper(r, server, server_username, send_to)

    server.quit()

