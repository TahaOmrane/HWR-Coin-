from app import create_app, db,socketio
from populate_questions import questions
from app.models import  QuizQuestion



app = create_app()



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if QuizQuestion.query.count() == 0:
            for q in questions:
                new_question = QuizQuestion(
                    question=q['question'],
                    option_a=q['option_a'],
                    option_b=q['option_b'],
                    option_c=q['option_c'],
                    option_d=q['option_d'],
                    correct_option=q['correct_option'],
                    category=q['category']
                )
                db.session.add(new_question)
            db.session.commit()
    socketio.run(app, debug=True)