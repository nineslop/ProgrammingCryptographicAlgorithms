import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from gost_r341094 import gost_r341094_ds_encrypt, gost_r341094_ds_decrypt, gost_r341094_ds_encrypt_check_parameters, gost_r341094_ds_decrypt_check_parameters
import random

class GOSTEncryptDecrypt(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GOST Encrypt / Decrypt')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.message_label = QLabel('Введите текст:')
        self.message_input = QLineEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        self.encrypt_button = QPushButton('Зашифровать')
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton('Дешифровать')
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def encrypt(self):
        open_text = self.message_input.text()
        alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        p = int(self.p_input.text())
        q = int(self.q_input.text())
        a = int(self.a_input.text())
        x = int(self.x_input.text())
        k = int(self.k_input.text())
        encrypted_text = gost_r341094_ds_encrypt(open_text, p, q, a, x, k, alphabet).split(" ")
        self.result_label.setText("Зашифровано: " + " ".join(encrypted_text))

def decrypt(self):
        encrypted_text = self.message_input.text()
        alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        p = int(self.p_input.text())
        q = int(self.q_input.text())
        a = int(self.a_input.text())
        y = int(self.y_input.text())
        ds = encrypted_text.split(" ")
        decrypted_text = gost_r341094_ds_decrypt('', p, q, a, y, ds, alphabet)
        self.result_label.setText("Дешифровано: " + decrypted_text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GOSTEncryptDecrypt()
    window.show()
    sys.exit(app.exec_())
