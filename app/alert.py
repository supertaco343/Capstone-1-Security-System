from flask_mail import Message
from app import app, mail

def send_email(recipient, subject, body):
    with app.app_context():
        msg = Message(subject, sender=app.config["MAIL_USERNAME"], recipients=[recipient])
        msg.body = body
        mail.send(msg)
