import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_remaining_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        next = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(next.text)
        category = next.category.replace(":", "")
        return  (category, next.difficulty, q_text, self.score , next.answer )
        #user = input(f"Q.{self.question_number}: {q_text} (True/False):  ")
        #self.check_answer(user, next.answer)

    def check_answer(self, user, correct_answer):
        if user.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
