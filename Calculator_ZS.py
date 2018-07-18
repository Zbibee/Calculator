import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QHBoxLayout, QGroupBox, QVBoxLayout, \
    QGridLayout
from functools import partial
import math

class Calc(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Zbigniew Smaza calculator'
        self.left = 200
        self.top = 200
        self.width = 720
        self.height = 480
        self.result = QTextEdit()
        self.number_to_print = 0
        self.value_float = False
        self.how_much = 0
        self.first_number = 0
        self.second_number = None
        self.results = None 
        self.push_action = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.result)
        windowLayout.addWidget(self.keyboard)
        self.setLayout(windowLayout)

        self.show()

    def createButtons(self):
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_0 = QPushButton('0')

        self.button_addition = QPushButton('+')
        self.button_subtraction = QPushButton('-')
        self.button_multiplication = QPushButton('*')
        self.button_division = QPushButton('/')
        self.button_result = QPushButton('=')
        self.button_reset = QPushButton('C')
        self.button_Backspace = QPushButton('Backspace')
        self.button_dot = QPushButton('.')
        self.button_sqrt = QPushButton('sqrt')
        self.button_power = QPushButton('^')

        self.button_1.clicked.connect(partial(self.push_number, number=1))
        self.button_2.clicked.connect(partial(self.push_number, number=2))
        self.button_3.clicked.connect(partial(self.push_number, number=3))
        self.button_4.clicked.connect(partial(self.push_number, number=4))
        self.button_5.clicked.connect(partial(self.push_number, number=5))
        self.button_6.clicked.connect(partial(self.push_number, number=6))
        self.button_7.clicked.connect(partial(self.push_number, number=7))
        self.button_8.clicked.connect(partial(self.push_number, number=8))
        self.button_9.clicked.connect(partial(self.push_number, number=9))
        self.button_0.clicked.connect(partial(self.push_number, number=0))
        self.button_dot.clicked.connect(partial(self.push_number, value_float = True))
        self.button_Backspace.clicked.connect(partial(self.push_number, Backspace = True))

        self.button_addition.clicked.connect(partial(self.action, action="addition"))
        self.button_subtraction.clicked.connect(partial(self.action, action="subtraction"))
        self.button_multiplication.clicked.connect(partial(self.action, action="multiplication"))
        self.button_division.clicked.connect(partial(self.action, action="division"))
        self.button_sqrt.clicked.connect(partial(self.action, action="sqrt"))
        self.button_power.clicked.connect(partial(self.action, action="power"))
        self.button_result.clicked.connect(self.print_result)
        self.button_reset.clicked.connect(self.reset)

    def createGridLayout(self):
        self.createButtons()
        self.keyboard = QGroupBox("Calc")
        layout = QGridLayout()

        layout.addWidget(self.button_1, 0, 0)
        layout.addWidget(self.button_2, 0, 1)
        layout.addWidget(self.button_3, 0, 2)
        layout.addWidget(self.button_addition, 0, 3)

        layout.addWidget(self.button_4, 1, 0)
        layout.addWidget(self.button_5, 1, 1)
        layout.addWidget(self.button_6, 1, 2)
        layout.addWidget(self.button_subtraction, 1, 3)

        layout.addWidget(self.button_7, 2, 0)
        layout.addWidget(self.button_8, 2, 1)
        layout.addWidget(self.button_9, 2, 2)
        layout.addWidget(self.button_multiplication, 2, 3)

        layout.addWidget(self.button_Backspace, 3, 0)
        layout.addWidget(self.button_dot, 3, 1)
        layout.addWidget(self.button_sqrt, 3, 2)
        layout.addWidget(self.button_power , 3, 3)
        
        layout.addWidget(self.button_reset, 4, 0)
        layout.addWidget(self.button_0, 4, 1)
        layout.addWidget(self.button_division, 4, 2)
        layout.addWidget(self.button_result, 4, 3)
        
        self.keyboard.setLayout(layout)


    def push_number(self, number=0 , value_float = False, Backspace = False):
        if value_float == True: #wlacz tryb zmienno przecinkowy
            self.value_float = True
        if value_float == False and Backspace == False:  #jezeli nie usuwasz lub nie zmieniasz trybu to wpisz liczbe
            if self.value_float == True:
                self.how_much += 1#wielkokrotnosc
                t = 10 ** -self.how_much
                self.number_to_print += number *t
                self.number_to_print = round(self.number_to_print, self.how_much)

            if self.value_float == False:
                self.number_to_print *= 10
                self.number_to_print += number

        if self.value_float == False and Backspace == True: # usun ostatnia liczbe
            self.number_to_print = int(self.number_to_print/10) #jezeli calkowita to usun ostatnia

        if self.value_float == True and Backspace == True:#jezeli zmienno przecinkowa to..
            self.how_much -= 1
            if self.how_much >= 1:
                self.number_to_print = self.number_to_print * (10 ** self.how_much)# 0.256 -> 25.6
                self.number_to_print = math.floor(self.number_to_print)#25.6 -> 25
                self.number_to_print = self.number_to_print / (10 ** self.how_much) # 25 -> 0.25
                
            if self.how_much == 0:
                self.value_float = False #jezeli dojdziemy do calkowitych to tryb calkowitychy
                self.number_to_print = math.floor(self.number_to_print)
            
        self.result.setText(str(self.number_to_print))

    def action(self, action):
        self.how_much = 1
        if action == "addition":
            self.result.setText("+")
        if action == "subtraction":
            self.result.setText("-")
        if action == "multiplication":
            self.result.setText("*")
        if action == "division":
            self.result.setText("/")
        if action == "sqrt":
            self.result.setText("sqrt({})".format(self.number_to_print))
        if action == "power":
            self.result.setText("^")
        self.action = action
        self.second_number = self.number_to_print
        self.number_to_print = 0
        self.value_float = False
        self.how_much = 0
        

    def print_result(self):
        if self.action == "addition":
            if self.results == None:
                self.results = self.second_number + self.number_to_print
                self.second_number = self.number_to_print
            elif self.results != None:
                    if self.results == self.number_to_print:
                        self.results = self.results + self.second_number
                    elif self.results != self.number_to_print:
                        self.results = self.results + self.number_to_print
                        self.second_number = self.number_to_print
                    
            self.number_to_print = self.results
            self.result.setText(str(self.results))

        if self.action == "subtraction":
            if self.results == None:
                self.results = self.second_number - self.number_to_print
                self.second_number = self.number_to_print
            elif self.results != None:
                    if self.results == self.number_to_print:
                        self.results = self.results - self.second_number
                    elif self.results != self.number_to_print:
                        self.results = self.results - self.number_to_print
                        self.second_number = self.number_to_print
                    
            self.number_to_print = self.results
            self.result.setText(str(self.results))

        if self.action == "multiplication":
            if self.results == None:
                self.results = self.second_number * self.number_to_print
                self.second_number = self.number_to_print
            elif self.results != None:
                    if self.results == self.number_to_print:
                        self.results = self.results * self.second_number
                    elif self.results != self.number_to_print:
                        self.results = self.results * self.number_to_print
                        self.second_number = self.number_to_print
                    
            self.number_to_print = self.results
            self.result.setText(str(self.results))

        if self.action == "division":
            if self.results == None:
                if self.number_to_print != 0:
                    self.results = self.second_number / self.number_to_print
                    self.second_number = self.number_to_print
                    self.number_to_print = self.results
                    self.result.setText(str(self.results))
                else:
                     self.result.setText("Nie dziel przez 0!")
            elif self.results != None:
                if self.number_to_print != 0:
                    if self.results == self.number_to_print:
                        self.results = self.results / self.second_number
                        self.number_to_print = self.results
                        self.result.setText(str(self.results))
                    elif self.results != self.number_to_print:
                        self.results = self.results / self.number_to_print
                        self.second_number = self.number_to_print
                        self.number_to_print = self.results
                        self.result.setText(str(self.results))
                else:
                     self.result.setText("Nie dziel przez 0!")
                                    
        if self.action == "power":
            if self.results == None:
                self.results = self.second_number ** self.number_to_print
                self.second_number = self.number_to_print
            elif self.results != None:
                    if self.results == self.number_to_print:
                        self.results = self.results ** self.second_number
                    elif self.results != self.number_to_print:
                        self.results = self.results ** self.number_to_print
                        self.second_number = self.number_to_print
                    
            self.number_to_print = self.results
            self.result.setText(str(self.results))

        if self.action == "sqrt":
            if self.second_number >=0:
                if self.results == None:
                    self.results = math.sqrt(self.second_number)
                    self.number_to_print = self.results
                    self.result.setText(str(self.results))
            else:
                self.result.setText("Nie możesz pierwiastkować liczby ujemnej!")

            if self.results != None:
                    if self.results >= 0:
                        if self.results == self.number_to_print:
                            self.results = math.sqrt(self.results)
                            self.number_to_print = self.results
                            self.result.setText(str(self.results))

                        elif self.results != self.number_to_print:
                            self.results = math.sqrt(self.second_number)
                            self.second_number = self.number_to_print
                            self.number_to_print = self.results
                            self.result.setText(str(self.results))
                    else:
                        self.result.setText("Nie możesz pierwiastkować liczby ujemnej!")
                    
    def reset(self):
        self.number_to_print = 0
        self.second_number = None
        self.results = None
        self.value_float = False
        self.how_much = 0
        self.result.setText(str(self.number_to_print))


app = QApplication(sys.argv)
ex = Calc()
sys.exit(app.exec_())
