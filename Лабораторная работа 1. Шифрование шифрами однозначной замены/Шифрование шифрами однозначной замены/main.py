import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QLineEdit # элементы интерфейса
from PyQt5.QtCore import Qt # импортируем константы и классы

class CipherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_mode = 0
        self.encryption_dict = {} # пустой словарь для хранения информации о шифрах и ключах

        self.initUI()

    def initUI(self): # пользовательский интерфейс
        input_label = QLabel('Введите текст:')
        self.input_text = QTextEdit()

        cipher_label = QLabel('Выберите шифр:')
        self.cipher_combobox = QComboBox()
        self.cipher_combobox.addItems(["Шифр Атбаш", "Шифр Цезаря", "Квадрат Полибия"])

        key_label = QLabel('Введите ключ (только для Шифра Цезаря):')
        self.key_entry = QLineEdit()

        encrypt_button = QPushButton('Зашифровать', self)
        encrypt_button.clicked.connect(self.on_encrypt_button_click)

        decrypt_button = QPushButton('Расшифровать', self)
        decrypt_button.clicked.connect(self.on_decrypt_button_click)

        toggle_button = QPushButton('Переключить режим', self)
        toggle_button.clicked.connect(self.toggle_mode)

        self.mode_label = QLabel('Режим: Обычный')

        output_label = QLabel('Результат:')
        self.output_text = QTextEdit()

        # Создание центрального виджета и установка компоновки
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(cipher_label)
        layout.addWidget(self.cipher_combobox)
        layout.addWidget(key_label)
        layout.addWidget(self.key_entry)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)
        layout.addWidget(toggle_button)
        layout.addWidget(self.mode_label)
        layout.addWidget(output_label)
        layout.addWidget(self.output_text)
        central_widget.setLayout(layout)

        # Установка центрального виджета в главное окно
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Шифры')
        self.setGeometry(100, 100, 640, 420)

    def caesar_cipher(self, input_str, key):
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        punctuations = {
            ",": "зпт",
            ".": "тчк",
            "-": "тире",
        }

        # Заменяем знаки препинания
        for original_char, replacement in punctuations.items():
            input_str = input_str.replace(original_char, replacement)

        result = ""
        for char in input_str:
            if char.isalpha(): # проверка является ли символ буквой
                is_upper = char.isupper() # является ли буква заглавной
                char = char.upper() # привод к верхнему регистру

                index = (alphabet.index(char) + key) % len(alphabet) # новый индекс символа
                new_char = alphabet[index]

                if not is_upper: # восстанавливаем регистр
                    new_char = new_char.lower()

                result += new_char
            else:
                result += char # символ не является буквой, оставляем его

        return result

    def atbash_cipher(self, input_str):
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        punctuations = {
            ",": "ЗПТ",
            ".": "ТЧК",
            "-": "ТИРЕ",
        }

        preprocessed_input = input_str.upper()
        for char, replacement in punctuations.items():
            preprocessed_input = preprocessed_input.replace(char, replacement)

        result = ""
        for char in preprocessed_input:
            if char.upper() in alphabet:
                index = alphabet.index(char.upper())
                new_char = alphabet[len(alphabet) - index - 1]
                if char.isupper():
                    result += new_char
                else:
                    result += new_char.lower()
            else:
                result += char

        return result

    def polybius_square_encrypt(self, input_str):
        square = [
            ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
            ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
            ['М', 'Н', 'О', 'П', 'Р', 'С'],
            ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
            ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
            ['Ю', 'Я', ',', '.', '-', ' '],
        ]

        input_without_spaces = input_str.replace(' ', '')

        result = ""
        for char in input_without_spaces.upper():
            found = False
            for i in range(len(square)):
                for j in range(len(square[i])):
                    if square[i][j] == char:
                        result += f'{i + 1}{j + 1}'
                        found = True
                        break
                if found:
                    break
            if not found:
                result += char

        return result

    def caesar_decipher(self, input_str, key):
        return self.caesar_cipher(input_str, -key)

    def atbash_decipher(self, input_str):
        return self.atbash_cipher(input_str)

    def polybius_square_decrypt(self, input_str):
        square = [
            ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
            ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
            ['М', 'Н', 'О', 'П', 'Р', 'С'],
            ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
            ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
            ['Ю', 'Я', ',', '.', '-', ' '],
        ]

        decrypted_text = ""
        i = 0
        while i < len(input_str):
            if input_str[i].isdigit() and i + 1 < len(input_str) and input_str[i + 1].isdigit():
                row = int(input_str[i])
                col = int(input_str[i + 1])
                if 1 <= row <= len(square) and 1 <= col <= len(square[row - 1]):
                    decrypted_text += square[row - 1][col - 1]
                else:
                    decrypted_text += input_str[i:i + 2]
                i += 2
            else:
                decrypted_text += input_str[i]
                i += 1

        return decrypted_text

    def extended_cipher(self, input_str, action):
        result = ""
        if action == "encrypt" and self.current_mode == 1:
            encryption_dict = {
                ",": "зпт",
                ".": "тчк",
                "-": "тире",
                "!": "вкз",
                "?": "впрз",
                ":": "двтч",
                ";": "тзчк",
                " ": "прбл",
                "\n": "рнрт",
            }

            for char in input_str:
                if char in encryption_dict:
                    result += encryption_dict[char]
                else:
                    result += char
        elif action == "decrypt" and self.current_mode == 1:
            decryption_dict = {
                "зпт": ",",
                "тчк": ".",
                "тире": "-",
                "вкз": "!",
                "впрз": "?",
                "двтч": ":",
                "тзчк": ";",
                "прбл": " ",
                "рнрт": "\n",
            }

            i = 0
            while i < len(input_str):
                found = False
                for key in decryption_dict:
                    if input_str[i:i+len(key)] == key:
                        result += decryption_dict[key]
                        i += len(key)
                        found = True
                        break
                if not found:
                    result += input_str[i]
                    i += 1
        else:
            return input_str

        return result



    def toggle_mode(self):
        self.current_mode = 1 - self.current_mode
        self.mode_label.setText("Режим: " + ("Обычный" if self.current_mode == 0 else "Расширенный"))

        if self.cipher_combobox.currentText() == "Расширенный":
            self.output_text.setPlainText("Выберите шифр")
        else:
            # Update the output based on the current mode
            text_to_process = self.input_text.toPlainText()
            if self.current_mode == 1:
                result = self.extended_cipher(text_to_process, action="encrypt")
            else:
                result = self.extended_cipher(text_to_process, action="decrypt")

            self.output_text.setPlainText(result)

    def on_encrypt_button_click(self):
        text_to_encrypt = self.input_text.toPlainText()
        selected_cipher = self.cipher_combobox.currentText()

        if selected_cipher == "Шифр Цезаря":
            key = int(self.key_entry.text())
            result = self.caesar_cipher(text_to_encrypt, key)
        elif selected_cipher == "Шифр Атбаш":
            result = self.atbash_cipher(text_to_encrypt)
        elif selected_cipher == "Квадрат Полибия":
            result = self.polybius_square_encrypt(text_to_encrypt)
        elif selected_cipher == "Расширенный":
            result = self.extended_cipher(text_to_encrypt)
        else:
            result = "Выберите шифр"

        self.output_text.setPlainText(result)

    def on_decrypt_button_click(self):
        text_to_decrypt = self.input_text.toPlainText()
        selected_cipher = self.cipher_combobox.currentText()

        if selected_cipher == "Шифр Цезаря":
            key = int(self.key_entry.text())
            result = self.caesar_decipher(text_to_decrypt, key)
        elif selected_cipher == "Шифр Атбаш":
            result = self.atbash_decipher(text_to_decrypt)
        elif selected_cipher == "Квадрат Полибия":
            result = self.polybius_square_decrypt(text_to_decrypt)
        elif selected_cipher == "Расширенный":
            result = self.extended_cipher(text_to_decrypt)
        else:
            result = "Выберите шифр"

        self.output_text.setPlainText(result)

if __name__ == '__main__':
    app = QApplication([])
    cipher_app = CipherApp()
    cipher_app.show()
    app.exec_()
