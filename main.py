from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from data import Question
from random import shuffle, choice
from PyQt5.QtGui import QStandardItem

app = QApplication([])

from main_window import *   
from menu_window import *

radio_list = [btn1, btn2, btn3, btn4]
shuffle (radio_list)
q1 = Question('2+2', '4', 'хто я', '6', 'петро')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Мишка', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
questions = [q1, q2, q3, q4]


def new_question():
    global cur_q
    cur_q = choice(questions)

    question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)

    shuffle(radio_list)

    radio_list[0].setText(cur_q.wrong_answer1)
    radio_list[1].setText(cur_q.wrong_answer2)
    radio_list[2].setText(cur_q.wrong_answer3)
    radio_list[3].setText(cur_q.answer)


new_question()
def show_menu():
    win_card.show()
    win_main.hide()


def back_menu():
    win_main.hide()
    win_card.show()

def check():
    for ans in radio_list:
        if ans.isChecked():
            if ans.text() == lb_correct.text():
                cur_q.got_right()
                lb_result.setText('Correct')
                break
    else:
        cur_q.got_right()
        lb_result.setText('Incorrect')


def click_ok():
    
    if checkBtn.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        ansGroupBox.show()

        checkBtn.setText('Наступне запитання')
    else:
        new_question()
        RadioGroupBox.show()
        ansGroupBox.hide()

        checkBtn.setText('Відповісти')
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)


btn_start.clicked.connect(show_menu)
menu_btn.clicked.connect(back_menu)
checkBtn.clicked.connect(click_ok)

win_card.hide()
win_main.show()
win_main.setStyleSheet('''
                      color: #0C356A;
                      background-color: #FFC436;
                      font-size: 20px;
                      border: 2px solid #FFF0CE;
                      ''')
app.exec_()