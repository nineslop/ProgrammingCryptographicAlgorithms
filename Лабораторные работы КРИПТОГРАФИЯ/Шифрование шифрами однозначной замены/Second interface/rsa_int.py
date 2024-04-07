import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QInputDialog
from RSAa import encode, decode, strToDigits, digitsToStr, isPrime, coprime, saveOutput, normalText, encodingFormat

class RSAApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Шифр RSA')
        self.resize(960, 640)
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Шифр RSA")
        layout.addWidget(title_label)

        # Ввод текста
        text_label = QLabel("Введите текст:")
        layout.addWidget(text_label)
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # Кнопки для шифрования и расшифрования
        encrypt_button = QPushButton("Зашифровать")
        encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(encrypt_button)

        decrypt_button = QPushButton("Расшифровать")
        decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(decrypt_button)

        # Поле для вывода результата
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def encrypt(self):
        text = self.text_edit.toPlainText()
        encoded_text = strToDigits(encodingFormat(text))

        # Ввод параметров p и q
        p, ok1 = QInputDialog.getInt(self, "Введите P", "Введите простое число p:")
        if not ok1:
            return
        if not isPrime(p):
            self.result_label.setText("Неверное p, оно должно быть простым")
            return

        q, ok2 = QInputDialog.getInt(self, "Введите Q", "Введите простое число q:")
        if not ok2:
            return
        if not isPrime(q):
            self.result_label.setText("Неверное q, оно должно быть простым")
            return

        n = p * q
        f = (p - 1) * (q - 1)

        # Ввод параметра e, взаимно простого с f
        e, ok3 = QInputDialog.getInt(self, "Введите E", "Введите случайное целое число e, взаимно простое с f:")
        if not ok3:
            return
        if not coprime(e, f):
            self.result_label.setText("Неверное e, оно должно быть взаимно простым с f")
            return

        result = encode(encoded_text, e, n)
        self.result_label.setText("Шифротекст: {}".format(result))

    def decrypt(self):
        text = self.text_edit.toPlainText()

        # Ввод параметров d и n
        d, ok1 = QInputDialog.getInt(self, "Введите D", "Введите d:")
        if not ok1:
            return

        n, ok2 = QInputDialog.getInt(self, "Введите N", "Введите n:")
        if not ok2:
            return

        result = normalText(digitsToStr(decode(text, d, n)))
        self.result_label.setText("Текст: {}".format(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RSAApp()
    ex.show()
    sys.exit(app.exec_())
