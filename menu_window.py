from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)


list_questions = QListView()
wdgt_edit = QWidget()
btn_start = QPushButton('Старт')

main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)
win_main = QWidget() 
win_main.resize(600, 500)

win_main.setLayout(layout_main)
