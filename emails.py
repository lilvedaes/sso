import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail_helper(r, server, send_from, to):

    body =\
    """
    <html>
        <body>
            <p>
                Somebody has sent you a message:
            </p>
            <ul>
                <label>Data:</label>
                <li>Email: {}</li>
                <li>Phone: {}</li>
                {}
            <ul>
        </body>
    </html>
    """.format(r["interested_name"],
               r["interested_email"],
               r["interested_cellphone"],
               r["interested_body"]
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
    send_to = "sso@utsc.utoronto.ca"
    server_username = "sso@utsc.utoronto.ca"
    server_password = "Spanish2018"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(server_username, server_password)

    send_mail_helper(r, server, server_username, send_to)

    server.quit()

