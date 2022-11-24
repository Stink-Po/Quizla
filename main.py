from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterFace

question_bank = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"], item["difficulty"], item["category"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterFace(quiz)
while quiz.still_remaining_question():
    quiz.next_question()
