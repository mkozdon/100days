from data import question_data
from question_model import Question
from random import choice
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

game = QuizBrain()
game.question_list = question_bank
while game.still_has_questions():
    game.next_question()
game.finish_quiz()
