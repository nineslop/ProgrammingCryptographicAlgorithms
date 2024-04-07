import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from RSA_DS import RSADSDecrypt, RSADSEncrypt, RSADSCheckParameters

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA DS Encryption/Decryption")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.message_input = QLineEdit()
        layout.addWidget(QLabel("Message:"))
        layout.addWidget(self.message_input)

        self.p_input = QLineEdit()
        layout.addWidget(QLabel("p:"))
        layout.addWidget(self.p_input)

        self.q_input = QLineEdit()
        layout.addWidget(QLabel("q:"))
        layout.addWidget(self.q_input)

        self.e_input = QLineEdit()
        layout.addWidget(QLabel("e:"))
        layout.addWidget(self.e_input)

        self.ds_input = QLineEdit()
        layout.addWidget(QLabel("ds:"))
        layout.addWidget(self.ds_input)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        encrypt_button = QPushButton("Encrypt")
        encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(encrypt_button)

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(decrypt_button)

        central_widget.setLayout(layout)

    def encrypt(self):
        open_text = self.message_input.text()
        p = int(self.p_input.text())
        q = int(self.q_input.text())
        e = int(self.e_input.text())
        alphabet = [chr(i) for i in range(ord('а'), ord('я')+1)]  # Assuming Russian alphabet
        encrypted_text = RSADSEncrypt(open_text, p, q, e, alphabet)
        self.result_label.setText(encrypted_text)

    def decrypt(self):
        encrypted_text = self.message_input.text()
        p = int(self.p_input.text())
        q = int(self.q_input.text())
        e = int(self.e_input.text())
        ds = int(self.ds_input.text())
        alphabet = [chr(i) for i in range(ord('а'), ord('я')+1)]  # Assuming Russian alphabet
        decrypted_text = RSADSDecrypt(encrypted_text, p, q, e, ds, alphabet)
        self.result_label.setText(decrypted_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
