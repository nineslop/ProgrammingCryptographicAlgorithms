import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QInputDialog, QMessageBox
from PyQt5.QtGui import QClipboard
from ELGAMALl import encode, decode, strToDigits, digitsToStr, isPrime, encodingFormat, saveOutput, testing, normalText


class ElgamalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Шифр Elgamal')
        self.resize(960, 640)
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Шифр Elgamal")
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

        # Кнопка для копирования результата
        copy_button = QPushButton("Копировать результат")
        copy_button.clicked.connect(self.copyResult)
        layout.addWidget(copy_button)

        self.setLayout(layout)

    def encrypt(self):
        # Ввод параметров P, G, X
        p, ok = QInputDialog.getInt(self, "Введите P", "Введите большое простое целое число P:")
        if not ok:
            return
        if not isPrime(p):
            self.result_label.setText("Число {} не является простым".format(p))
            return

        g, ok = QInputDialog.getInt(self, "Введите G", "Введите большое целое G, при этом G > 1 и G < P:")
        if not ok:
            return
        if g <= 1 or g >= p:
            self.result_label.setText("Число {} не удовлетворяет G > 1 и G < P".format(g))
            return

        x, ok = QInputDialog.getInt(self, "Введите X", "Введите большое целое X, при этом X > 1 и X < P:")
        if not ok:
            return
        if x <= 1 or x >= p:
            self.result_label.setText("Число {} не удовлетворяет X > 1 и X < P".format(x))
            return

        # Шифрование текста
        text = self.text_edit.toPlainText()
        encoded_text = strToDigits(encodingFormat(text))
        result = encode(encoded_text, p, g, x)
        self.result_label.setText("Шифротекст: {}".format(result))

    def decrypt(self):
        # Ввод параметров P, X
        p, ok = QInputDialog.getInt(self, "Введите P", "Введите большое простое целое число P:")
        if not ok:
            return
        if not isPrime(p):
            self.result_label.setText("Число {} не является простым".format(p))
            return

        x, ok = QInputDialog.getInt(self, "Введите X", "Введите большое целое X, при этом X > 1 и X < P:")
        if not ok:
            return
        if x <= 1 or x >= p:
            self.result_label.setText("Число {} не удовлетворяет X > 1 и X < P".format(x))
            return

        # Расшифрование текста
        text = self.text_edit.toPlainText()
        result = normalText(digitsToStr(decode(text, p, x)))
        self.result_label.setText("Текст: {}".format(result))

    def copyResult(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result_label.text())
        QMessageBox.information(self, "Копирование", "Результат скопирован в буфер обмена")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElgamalApp()
    ex.show()
    sys.exit(app.exec_())
