import emails
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def show_page():
    if request.method == 'POST':
        emails.send_mail(request.values)
        return "", 204

    return render_template("index.html")


if __name__ == '__main__':
    app.run()