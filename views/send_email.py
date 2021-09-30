from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'lgpdcompliantwebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'LGPD-compliant2020'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_ASCII_ATTACHMENT'] = False

mail = Mail(app)

@app.route('/')
def sendMail(to,subject,template):
    msg = Message(subject=subject, sender='lgpdcompliantwebsite@gmail.com', recipients=to)
    msg.body(template)
    mail.send(msg)
    return 'Message Sent'


if __name__ == "__main__":
    app.run(debug=False)