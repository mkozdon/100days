class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = []
        self.correct_answers = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {question.text} (True/False)?: ")
        self.question_number += 1
        if answer == question.answer:
            self.correct_answers += 1
            print("You've got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {question.answer}")
        print(
            f"Your current score is: {self.correct_answers}/{self.question_number}\n\n"
        )

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def finish_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.correct_answers}/{self.question_number} ")
