import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
from atbash import atbash_encrypt, atbash_decrypt
from cesar import cesar_encrypt, cesar_decrypt, cesar_check_parameters
from polibia import polibia_encrypt, polibia_decrypt
from tritemiy import tritemiy_encrypt, tritemiy_decrypt
from belazo import belazo_encrypt, belazo_decrypt, belazo_check_parameters
from vigener import vigener_encrypt, vigener_decrypt, vigener_check_parameters
from matrix import matrix_encrypt, matrix_decrypt, matrix_check_parameters
from playfair import playfair_encrypt, playfair_decrypt, playfair_check_parameters

available_ciphers = [
    "Шифр АТБАШ", "Шифр Цезаря", "Шифр Полибия",
    "Шифр Тритемия", "Шифр Белазо", "Шифр Виженера",
    "Шифр Матричный", "Шифр Плейфера",
]

alphabet = [
    "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м",
    "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ",
    "ъ", "ы", "ь", "э", "ю", "я"
]

alphabet_polibia = [
    ["а", "б", "в", "г", "д", "е"],
    ["ж", "з", "и", "й", "к", "л"],
    ["м", "н", "о", "п", "р", "с"],
    ["т", "у", "ф", "х", "ц", "ч"],
    ["ш", "щ", "ъ", "ы", "ь", "э"],
    ["ю", "я"]
]

alphabet_playfair = [
    "а", "б", "в", "г", "д", "е", "ж", "з", "и", "к", "л", "м", "н",
    "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь",
    "ы", "э", "ю", "я"
]

mem = {
    "bigTextFlag": False,
    "vigenerSwitch": False,
    "mode": "encrypt",
}

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Шифры')
        layout = QVBoxLayout()

        # Выбор шифра
        self.cipher_label = QLabel('Выберите шифр:')
        self.cipher_combo = QComboBox()
        self.cipher_combo.addItems(available_ciphers)

        # Ввод открытого текста
        self.open_text_label = QLabel('Введите открытый текст:')
        self.open_text_edit = QTextEdit()

        # Ввод зашифрованного текста
        self.cipher_text_label = QLabel('Введите зашифрованный текст:')
        self.cipher_text_edit = QTextEdit()

        # Ввод сдвига для шифра Цезаря
        self.cesar_shift_label = QLabel('Введите сдвиг для шифра Цезаря:')
        self.cesar_shift_edit = QLineEdit()

        # Ввод ключевого слова для шифра Белазо или Плейфера
        self.keyword_label = QLabel('Введите ключевое слово для шифра Белазо или Плейфера:')
        self.keyword_edit = QLineEdit()

        # Ввод ключевой буквы для шифра Виженера
        self.vigener_key_label = QLabel('Введите ключевую букву для шифра Виженера:')
        self.vigener_key_edit = QLineEdit()

        # Ввод ключевой матрицы для шифра Матричный
        self.matrix_label = QLabel('Введите ключевую матрицу для шифра Матричный:')
        self.matrix_edit = QLineEdit()

        # Режим работы шифра (шифрование или дешифрование)
        self.mode_label = QLabel('Выберите режим:')
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Шифрование', 'Дешифрование'])

        # Кнопка для запуска шифрования/дешифрования
        self.encrypt_button = QPushButton('Выполнить')

        layout.addWidget(self.cipher_label)
        layout.addWidget(self.cipher_combo)
        layout.addWidget(self.open_text_label)
        layout.addWidget(self.open_text_edit)
        layout.addWidget(self.cipher_text_label)
        layout.addWidget(self.cipher_text_edit)
        layout.addWidget(self.cesar_shift_label)
        layout.addWidget(self.cesar_shift_edit)
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.keyword_edit)
        layout.addWidget(self.vigener_key_label)
        layout.addWidget(self.vigener_key_edit)
        layout.addWidget(self.matrix_label)
        layout.addWidget(self.matrix_edit)
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.encrypt_button)

        self.setLayout(layout)

        # Подключение слотов к сигналам
        self.encrypt_button.clicked.connect(self.cipher_parser)

    def text_preparation(self, text):
        bigTextFlag = False  # TODO: Добавить обработку флага
        if bigTextFlag:
            return text.replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "прбл").replace(":", "двтч").replace(";", "тчсзп").replace("(", "отскб").replace(")", "зкскб").replace("?", "впрзн").replace("!", "восклзн").replace("\n", "првст").lower()
        else:
            return text.replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "").replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("?", "").replace("!", "").replace("\n", "").lower()

    def cipher_parser(self):
        cipher_choose_input = self.cipher_combo.currentText()
        open_text_input = self.open_text_edit.toPlainText()
        cipher_text_input = self.cipher_text_edit.toPlainText()
        cesar_shift = self.cesar_shift_edit.text()
        keyword = self.keyword_edit.text()
        vigener_keyletter = self.vigener_key_edit.text()
        matrix_input = self.matrix_edit.text()

        # Определение режима работы (шифрование или дешифрование)
        mode = 'encrypt' if self.mode_combo.currentText() == 'Шифрование' else 'decrypt'

        if cipher_choose_input == "Шифр АТБАШ":
            if mode == "encrypt":
                cipher_text_input = atbash_encrypt(self.text_preparation(open_text_input), alphabet)
            elif mode == "decrypt":
                open_text_input = atbash_decrypt(cipher_text_input, alphabet)
        elif cipher_choose_input == "Шифр Цезаря":
            if cesar_shift:  # Проверка на пустую строку
                cesar_shift = int(cesar_shift)
                if cesar_check_parameters(cesar_shift, alphabet):
                    if mode == "encrypt":
                        cipher_text_input = cesar_encrypt(self.text_preparation(open_text_input), cesar_shift, alphabet)
                    elif mode == "decrypt":
                        open_text_input = cesar_decrypt(cipher_text_input, cesar_shift, alphabet)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ввода сдвига"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ввода сдвига"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите сдвиг для шифра Цезаря"
                elif mode == "decrypt":
                    open_text_input = "Введите сдвиг для шифра Цезаря"
        elif cipher_choose_input == "Шифр Полибия":
            if mode == "encrypt":
                cipher_text_input = polibia_encrypt(self.text_preparation(open_text_input), alphabet_polibia)
            elif mode == "decrypt":
                open_text_input = polibia_decrypt(cipher_text_input, alphabet_polibia)
        elif cipher_choose_input == "Шифр Тритемия":
            if mode == "encrypt":
                cipher_text_input = tritemiy_encrypt(self.text_preparation(open_text_input), alphabet)
            elif mode == "decrypt":
                open_text_input = tritemiy_decrypt(cipher_text_input, alphabet)
        elif cipher_choose_input == "Шифр Белазо":
            if keyword:
                if belazo_check_parameters(keyword.lower(), alphabet):
                    if mode == "encrypt":
                        cipher_text_input = belazo_encrypt(self.text_preparation(open_text_input), keyword.lower(), alphabet)
                    elif mode == "decrypt":
                        open_text_input = belazo_decrypt(cipher_text_input, keyword.lower(), alphabet)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ввода ключевого слова"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ввода ключевого слова"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевое слово для шифра Белазо"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевое слово для шифра Белазо"
        elif cipher_choose_input == "Шифр Виженера":
            if vigener_keyletter:
                if vigener_check_parameters(vigener_keyletter, alphabet):
                    if mode == "encrypt":
                        # Измените эту строку
                        cipher_text_input = vigener_encrypt(self.text_preparation(open_text_input), vigener_keyletter, alphabet)
                    elif mode == "decrypt":
                        # И измените эту строку
                        open_text_input = vigener_decrypt(cipher_text_input, vigener_keyletter, alphabet)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ввода ключевой буквы"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ввода ключевой буквы"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевую букву для шифра Виженера"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевую букву для шифра Виженера"
        elif cipher_choose_input == "Шифр Матричный":
            if matrix_input:
                if matrix_check_parameters(matrix_input):
                    if mode == "encrypt":
                        cipher_text_input = matrix_encrypt(self.text_preparation(open_text_input), matrix_input)
                    elif mode == "decrypt":
                        open_text_input = matrix_decrypt(cipher_text_input, matrix_input)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ввода матрицы"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ввода матрицы"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевую матрицу для шифра Матричный"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевую матрицу для шифра Матричный"
        elif cipher_choose_input == "Шифр Плейфера":
            if keyword:
                if playfair_check_parameters(keyword, alphabet_playfair):
                    if mode == "encrypt":
                        cipher_text_input = playfair_encrypt(self.text_preparation(open_text_input), keyword, alphabet_playfair)
                    elif mode == "decrypt":
                        open_text_input = playfair_decrypt(cipher_text_input, keyword, alphabet_playfair)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ввода ключевого слова"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ввода ключевого слова"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевое слово для шифра Плейфера"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевое слово для шифра Плейфера"
        # Добавьте обработку остальных шифров здесь
        else:
            pass

        # Обновление текста в виджетах
        self.open_text_edit.setPlainText(open_text_input)
        self.cipher_text_edit.setPlainText(cipher_text_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CipherApp()
    ex.show()
    sys.exit(app.exec_())
