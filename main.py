from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from guess_number import Ui_GuessNumber
import random

class GuessNumberWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.game=Ui_GuessNumber()
        self.game.setupUi(self)
        self.game.stackedWidget.setCurrentWidget(self.game.welcome_page)
        self.show()
        
        # change cerrunt page
        self.game.start_btn.clicked.connect(lambda :self.game.stackedWidget.setCurrentWidget(self.game.game_page))
        self.game.play_again_btn.clicked.connect(lambda :self.game.stackedWidget.setCurrentWidget(self.game.welcome_page))
        
        # controls buttons
        self.game.bigger_btn.clicked.connect(self.bigger_guess_number)
        self.game.smaller_btn.clicked.connect(self.smaller_guess_number)
        self.game.correct_btn.clicked.connect(self.correct_guess_number)

       
        self.start,self.end=0,100
        self.guessed_number=random.randint(self.start,self.end)
        self.game.guessed_number.setText(str(self.guessed_number))
    
    # functions for guide the compuetr to guess the number
    def bigger_guess_number(self):
        self.end=self.guessed_number-1
        self.guessed_number=random.randint(self.start,self.end)
        self.game.guessed_number.setText(str(self.guessed_number))  
    
    def smaller_guess_number(self):
        self.start=self.guessed_number+1
        self.guessed_number=random.randint(self.start,self.end)
        self.game.guessed_number.setText(str(self.guessed_number))

    def correct_guess_number(self):
       self.game.stackedWidget.setCurrentWidget(self.game.finish_page)
        



if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window=GuessNumberWindow()
    sys.exit(app.exec_())




