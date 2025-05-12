from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(10), nullable=False)  # 'email' or 'sms'
