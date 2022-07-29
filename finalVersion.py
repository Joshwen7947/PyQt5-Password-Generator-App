import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QVBoxLayout, QPushButton, QLabel
import random


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(100,100, 400, 400)
        self.intro = QLabel("Welcome to PyPass Gen 2.0")
        self.dialog1 = QInputDialog()
        self.dialog1.setOption(QInputDialog.NoButtons)
        self.dialog1.setLabelText('Number of passwords: ')
        self.dialog2 = QInputDialog()
        self.dialog2.setOption(QInputDialog.NoButtons)
        self.dialog2.setLabelText('Length of passwords: ')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.intro, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.dialog1)
        self.layout.addWidget(self.dialog2)
        self.alert = QLabel()
        self.textBox = QLabel()
        self.layout.addWidget(self.alert, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.textBox, alignment=Qt.AlignCenter)
        self.button1 = QPushButton("Generate Passwords")
        self.button1.clicked.connect(self.execute)
        self.layout.addWidget(self.button1)

        self.setLayout(self.layout)
        self.show()

    def execute(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_,./?'
        number_v = int(self.dialog1.textValue())
        length_v = int(self.dialog2.textValue())
        passwords = []
        for count in range(number_v):
            password = ''.join(random.choices(chars, k=length_v))
            passwords.append(password)
        self.alert.setText(f'Here are {number_v} unique passwords:')
        self.textBox.setText('\n'.join(passwords))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())