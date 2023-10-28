
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.is_active = True
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        self.attempts += 1


class QuestionView():
    def __init__ (self,question_model, question, right_ans, wrong_ans_1, wrong_ans_2, wrong_ans_3):

        self.question_model = question_model

        self.question  = question
        self.right_ans = right_ans
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3

    def change (self, question_model):
        self.question_model = question_model

    
    def show (self):
        self.question.setText(self.question_model.question)
        self.right_ans.setText(self.question_model.right_ans)
        self.wrong_ans_1.setText(self.question_model.wrong_ans_1)
        self.wrong_ans_2.setText(self.question_model.wrong_ans_2)
        self.wrong_ans_3.setText(self.question_model.wrong_ans_3)

