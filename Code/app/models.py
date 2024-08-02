from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=0)
    password = db.Column(db.String(60), nullable=False)
    unlocked_intermediate1 = db.Column(db.Boolean, default=False)
    unlocked_intermediate2 = db.Column(db.Boolean, default=False)
    unlocked_hard = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(256), nullable=False)
    option_b = db.Column(db.String(256), nullable=False)
    option_c = db.Column(db.String(256), nullable=False)
    option_d = db.Column(db.String(256), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # New field for category

    def __repr__(self):
        return f'<QuizQuestion {self.question}>'
