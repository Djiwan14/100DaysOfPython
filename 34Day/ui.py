from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quiz_Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label = Label(text=f"Score = 0")
        self.score_label.grid(row=0, column=1)
        # canvas text
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Lorem ipsum", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        # true button
        self.img_of_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.img_of_true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        # false button
        self.img_of_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.img_of_false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self,):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
