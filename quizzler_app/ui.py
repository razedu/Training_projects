import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = tk.Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.score = tk.Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        true_img = tk.PhotoImage(file="images/true.png")
        self.but_true = tk.Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.but_true.grid(column=0, row=2)

        false_img = tk.PhotoImage(file="images/false.png")
        self.but_false = tk.Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.but_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The End.")
            self.but_false.config(state="disabled")
            self.but_true.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
