from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User,QuizQuestion
from app import socketio
import requests


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ihr Konto wurde erstellt! Sie können sich jetzt anmelden', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
    response = requests.get(url, params=params)
    return response.json()

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(target=send_crypto_data)

def send_crypto_data():
    while True:
        data = fetch_crypto_data()
        socketio.emit('crypto_data', data)
        socketio.sleep(10)  # Fetch data every 10 seconds


@main.route('/articles')
@login_required
def articles():
    return render_template('articles.html', articles=articles)

@main.route('/quizzes')
@login_required
def quizzes():
    return render_template('quiz_select.html')
@main.route('/graphs')
@login_required
def graphs():
    return render_template('graph.html')
@main.route('/quiz/<level>', methods=['GET', 'POST'])
@login_required
def quiz(level):
    # Define a dictionary to map levels to categories
    level_to_category = {
        'easy': 'Easy',
        'intermediate1': 'Intermediate1',
        'intermediate2': 'Intermediate2',
        'hard': 'Hard'
    }

    # Get the category for the given level
    category = level_to_category.get(level, 'Easy')  # Default to 'Easy' if level not found
    # Query the database to get questions of the specified category
    questions = QuizQuestion.query.filter_by(category=category).all()
    print(level,";llllll")
    if request.method == 'POST':
        print("insideeeeee")
        score = 0
        for question in questions:
            # Get the submitted answer from the form
            submitted_answer = request.form.get(f'question_{question.id}')
            result_answer=''
            # Check if the submitted answer matches the correct option
            if(question.correct_option=="A"):
                result_answer=question.option_a
            elif(question.correct_option=="B"):
                result_answer=question.option_b
            elif(question.correct_option=="C"):
                result_answer=question.option_c
            elif(question.correct_option=="D"):
                result_answer=question.option_d
            if submitted_answer == result_answer:
                score += 1
        
        if score >= 15:
            print(score)
            print(level,"level")
            if level == 'easy' and not current_user.unlocked_intermediate1:
                current_user.unlocked_intermediate1 = True
            elif level == 'intermediate1' and not current_user.unlocked_intermediate2:
                current_user.unlocked_intermediate2 = True
            elif level == 'intermediate2' and not current_user.unlocked_hard:
                current_user.unlocked_hard = True
            db.session.commit()
        print(current_user.points,"points")
        current_user.points = max(current_user.points, score)
        print(current_user.points,"points")
        db.session.commit()

        if level == 'easy' and score >= 15:
            current_user.level = max(current_user.level, 1)
        elif level == 'intermediate1' and score >= 15:
            current_user.level = max(current_user.level, 2)
        elif level == 'intermediate2' and score >= 15:
            current_user.level = max(current_user.level, 3)
        db.session.commit()

        return render_template('quiz_result.html', score=score, total=len(questions))

    # Convert questions to a format suitable for rendering in the template
    formatted_questions = [
        {
            "question": q.question,
            "options": [q.option_a, q.option_b, q.option_c, q.option_d],
            "answer": q.correct_option,
            "id": q.id
        }
        for q in questions
    ]

    return render_template('quiz.html', questions=formatted_questions, level=level)


@main.route('/article/<level>', methods=['GET', 'POST'])
@login_required
def article(level):
   if (level=="easy"):
        return render_template('articles/easy.html')
   elif(level=="medium"):
        return render_template('articles/medium.html')
   else:
       return render_template('articles/hard.html') 

