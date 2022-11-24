from tkinter import *
from quiz_brain import QuizBrain

COLOR = "#375362"
text_map = []
correct_answer = ""
FONT = ("Zippy", 20)
keep = None
press = True


class QuizInterFace:

    def __init__(self, quizz_brain: QuizBrain):
        self.quizz = quizz_brain
        self.text = ""
        self.count = 0
        self.keep = None
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=50, padx=50, bg=COLOR)
        self.category_label = Label(text="Category", bg=COLOR, fg="white", font=FONT)
        self.score_label = Label(text="Score", bg=COLOR, fg="white", font=FONT)
        self.canvas = Canvas(height=360, width=400)
        self.question_text = self.canvas.create_text(180, 200, text="Some text", font=("arial", 20, "italic"),
                                                     fill=COLOR, width=270)
        self.category_label.grid(column=0, row=1, columnspan=2)
        self.score_label.grid(column=0, row=0, columnspan=2)
        self.difficulty_label = Label(bg=COLOR, fg="white", font=FONT)
        self.difficulty_label.grid(column=0, row=2, columnspan=2)
        self.canvas.grid(column=0, row=3, columnspan=2, pady=50)
        self.true_image = PhotoImage(file="true.png")
        self.false_image = PhotoImage(file="false.png")
        self.button = IntVar()
        self.true_button = Button(image=self.true_image, highlightthickness=0, activebackground=COLOR,
                                  command=self.true_press, textvariable=self.button)
        self.false_button = Button(image=self.false_image, highlightthickness=0, activebackground=COLOR,
                                   command=self.false_press, textvariable=self.button)
        self.true_button.grid(column=0, row=4)
        self.false_button.grid(column=1, row=4)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        global text_map, correct_answer, press
        press = True
        if self.quizz.still_remaining_question():
            self.canvas.config(bg="white")
            question = self.quizz.next_question()
            list_name = list(question)
            text_map = list_name
            text_map = list_name[2]
            category = list_name[0]
            difficulty = list_name[1]
            correct_answer = list_name[4]
            self.category_label.config(text=f"Category :   {category.title()}")
            self.difficulty_label.config(text=f"Difficulty :   {difficulty.title()}")
            self.score_label.config(text=f"Score :   {self.quizz.score} / {self.quizz.question_number - 1}")
            self.write()
        else:
            self.canvas.itemconfig(self.question_text, text=f"You rich the end of the Quizz your final Score is:"
                                                            f"{self.quizz.score}/{self.quizz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def write(self):
        if press:
            self.canvas.itemconfig(self.question_text, text=self.text)
            if len(self.text) != len(text_map):
                self.text += text_map[self.count]
                self.count += 1
                self.keep = self.window.after(100, self.write)
            else:
                self.count = 0
                self.text = ""
                return
        else:
            self.count = 0
            self.text = ""

            self.window.after_cancel(self.keep)
            self.window.after(100, self.get_next_question)
            return

    def true_press(self):
        global press
        press = False
        self.count = 0
        self.text = ""
        is_right = self.quizz.check_answer("True", correct_answer)
        self.feed_back(is_right)

    def false_press(self):
        global press
        press = False
        self.count = 0
        self.text = ""
        is_right = self.quizz.check_answer("False", correct_answer)
        self.feed_back(is_right)

    def feed_back(self, is_right):
        if is_right:
            self.window.after_cancel(self.keep)
            self.canvas.itemconfig(self.question_text, text="Correct")
            self.window.after(1000, self.get_next_question)
        else:
            self.window.after_cancel(self.keep)
            self.canvas.itemconfig(self.question_text, text="Wrong")
            self.window.after(1000, self.get_next_question)
