import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow ,  QMessageBox ,QGroupBox , QRadioButton ,QTextEdit
from PySide6.QtUiTools import QUiLoader
from ui_password import Ui_MainWindow 
from functools import partial

class PasswordGenerator(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.generate = self.ui.generate_btn
        self.result_box = self.ui.box
        self.standard = self.ui.rb_standard
        self.extra = self.ui.rb_extra
        self.super = self.ui.rb_super

        self.standard.clicked.connect(partial(self.select_mode , "standard"))
        self.extra.clicked.connect(partial(self.select_mode , "extra"))
        self.super.clicked.connect(partial(self.select_mode , "super"))
        self.generate.clicked.connect(self.generate_pass)

    def createGroup(self):
        groupBox = QGroupBox()

        self.standard = QRadioButton("Radiobutton 1")
        self.extra = QRadioButton("Radiobutton 2")
        self.super = QRadioButton("Radiobutton 3")

        self.standard.setChecked(True)
        return groupBox

    def select_mode (self,input):
        global mode 
        mode = input
        return mode        

    def generate_pass(self):
        global mode
        self.standard.setChecked(True)
        self.extra.setChecked(False)
        self.super.setChecked(False)
        self.digits = ['0','1','2','3','4','5','6','7','8','9']
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.symbols = ['@','#','$','%','&','*','!',':','+','/','?','<','>','-']
        self.up_char = list((self.alphabet[i].upper()  for i in range(len(self.alphabet)-1) ))
        self.final_password =[]

        if mode == "standard" :
            # pass length = 8
            for digits in range(0,3):
                self.final_password.append(random.choice(self.digits))
            for alphabet in range(0,2):
                self.final_password.append(random.choice(self.alphabet))
            for uper_c in range(0,3):
                self.final_password.append(random.choice(self.up_char))

            self.password=random.shuffle(self.final_password)
            self.password_string =(''.join(self.final_password))

            self.result_box.setPlainText(self.password_string)


        elif mode == "extra" :
            self.standard.setChecked(False)
            self.extra.setChecked(True)
            self.super.setChecked(False)            
            # pass length = 12
            for digits in range(0,3):
                self.final_password.append(random.choice(self.digits))
            for alphabet in range(0,3):
                self.final_password.append(random.choice(self.alphabet))
            for uper_c in range(0,3):
                self.final_password.append(random.choice(self.up_char))
            for symbols in range(0,3):
                self.final_password.append(random.choice(self.symbols))

            self.password=random.shuffle(self.final_password)
            self.password_string = (''.join(self.final_password))

            self.result_box.setPlainText(self.password_string)

        elif mode == "super" :
            self.standard.setChecked(False)
            self.extra.setChecked(False)
            self.super.setChecked(True)            
            # pass length = 20
            for digits in range(0,4):
                self.final_password.append(random.choice(self.digits))
            for alphabet in range(0,4):
                self.final_password.append(random.choice(self.alphabet))
            for uper_c in range(0,4):
                self.final_password.append(random.choice(self.up_char))
            for symbols in range(0,7):
                self.final_password.append(random.choice(self.symbols))

            self.password=random.shuffle(self.final_password)
            self.password_string = (''.join(self.final_password))

            self.result_box.setPlainText(self.password_string)



app = QApplication(sys.argv)
main_window = PasswordGenerator()
main_window.show()



app.exec()