import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QCheckBox
from PyQt5.QtCore import Qt
from atbash import atbash_encrypt, atbash_decrypt
from cesar import cesar_encrypt, cesar_decrypt, cesar_check_parameters
from polibia import polibia_encrypt, polibia_decrypt
from tritemiy import tritemiy_encrypt, tritemiy_decrypt
from belazo import belazo_encrypt, belazo_decrypt, belazo_check_parameters
from vigener import vigener_encrypt, vigener_decrypt, vigener_check_parameters
from S_block import s_block_check_parameters,s_block_encrypt, s_block_decrypt
from matrix import matrix_encrypt, matrix_decrypt, matrix_check_parameters
from playfair import playfair_encrypt, playfair_decrypt, playfair_check_parameters
from veritcalTransposition import vertical_transposition_check_parameters, vertical_transposition_encrypt, vertical_transposition_decrypt
from cardanosGrid import cardanosGridCheckParameters, cardanosGridEncrypt, cardanosGridDecrypt
from feistelsNetwork import feistelsNetworkCheckParameters, feistelsNetwork
from shannons_notebook import shannonsNotebookCheckParameters, shannonsNotebookEncrypt, shannonsNotebookDecrypt
from hexoize import StrToHex, HexToStr
from magma import MagmaCheckParameters, magma
from A5 import A5CheckParameters, A51, A52

available_ciphers = [
    "Шифр АТБАШ", "Шифр Цезаря", "Шифр Полибия",
    "Шифр Тритемия", "Шифр Белазо", "Шифр Виженера", "МАГМА(s_block)",
    "Шифр Матричный", "Шифр Плейфера", "Шифр вертикальной перестановки",
    "Шифр решетка Кардано", "Шифр сеть Фейстель", "Одноразовый блокнот Шеннона",
    "Hexoize", "Магма (гаммирование)", "A5/1", "A5/2",
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

alphabet_sblock = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]


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
        self.resize(960, 640)
        layout = QVBoxLayout()

        # Выбор шифра
        cipher_layout = QHBoxLayout()
        cipher_label = QLabel('Выберите шифр:')
        self.cipher_combo = QComboBox()
        self.cipher_combo.addItems(available_ciphers)
        cipher_layout.addWidget(cipher_label)
        cipher_layout.addWidget(self.cipher_combo)

        # Ввод открытого текста
        open_text_label = QLabel('Введите открытый текст(Расшифрованный):')
        self.open_text_edit = QTextEdit()

        # Ввод зашифрованного текста
        cipher_text_label = QLabel('Шифрованный текст:')
        self.cipher_text_edit = QTextEdit()

        # Ввод сдвига для шифра Цезаря
        self.cesar_shift_edit = QLineEdit()
        self.cesar_shift_edit.setPlaceholderText('Введите сдвиг для шифра Цезаря')
        self.cesar_shift_edit.textChanged.connect(self.check_cesar_shift)

        # Ввод ключевого слова для шифра Белазо или Плейфера
        self.keyword_edit = QLineEdit()
        self.keyword_edit.setPlaceholderText('Введите ключевое слово для шифра Белазо, Плейфера, Вертикальной перестановки')

        # Ввод ключевой буквы для шифра Виженера
        self.vigener_key_edit = QLineEdit()
        self.vigener_key_edit.setPlaceholderText('Введите ключевую букву для шифра Виженера')
        self.vigener_key_edit.textChanged.connect(self.check_vigener_key)

        # Ввод ключевой матрицы для шифра Матричный
        self.matrix_edit = QLineEdit()
        self.matrix_edit.setPlaceholderText('Введите ключевую матрицу для шифра Матричный')

        # Ввод размерности решётки для шифра Кардано
        self.cardanosGrid_edit = QLineEdit()
        self.cardanosGrid_edit.setPlaceholderText('Введите размерность решётки для шифра Кардано (8 8)')

        # Ввод решётки для шифра Кардано
        self.cardanosGridGRIDGRID_edit = QLineEdit()
        self.cardanosGridGRIDGRID_edit.setPlaceholderText('Решётка (0 1, 1 6, 2 1, 2 2, 2 4, 3 6, 3 7, 4 3, 4 5, 5 0, 6 3, 6 5, 6 7, 7 2, 7 4, 7 7)')

        # Ввод решётки для шифра сеть Фейстеля
        self.feistelsNet_edit = QLineEdit()
        self.feistelsNet_edit.setPlaceholderText('Ключ для шифра сети Фейстеля')

        # Ввод t для Одноразового блокнота Шеннона
        self.shannons_t_a_c_edit = QLineEdit()
        self.shannons_t_a_c_edit.setPlaceholderText('t a c для Одноразового блокнота Шеннона')

        # Ввод ключа для Магмы (гаммирования)
        self.magmaKeyInput_edit = QLineEdit()
        self.magmaKeyInput_edit.setPlaceholderText('Ключ для Магма(гаммирования)')

        # Ввод Инициализирующий вектор
        self.magmaVectorInput_edit = QLineEdit()
        self.magmaVectorInput_edit.setPlaceholderText('Инициализирующий вектор для Магма(гаммирования)')

        self.A5key_edit = QLineEdit()
        self.A5key_edit.setPlaceholderText('Ключ для A5/1 и A5/2')

        # Режим работы шифра (шифрование или дешифрование)
        mode_layout = QHBoxLayout()
        mode_label = QLabel('Выберите режим:')
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Шифрование', 'Расшифрование'])
        mode_layout.addWidget(mode_label)
        mode_layout.addWidget(self.mode_combo)

        # Кнопка для запуска шифрования/дешифрования
        self.encrypt_button = QPushButton('Выполнить')

        layout.addLayout(cipher_layout)
        layout.addWidget(open_text_label)
        layout.addWidget(self.open_text_edit)
        layout.addWidget(cipher_text_label)
        layout.addWidget(self.cipher_text_edit)
        layout.addWidget(self.cesar_shift_edit)
        layout.addWidget(self.keyword_edit)
        layout.addWidget(self.vigener_key_edit)
        layout.addWidget(self.matrix_edit)
        layout.addWidget(self.cardanosGrid_edit)
        layout.addWidget(self.cardanosGridGRIDGRID_edit)
        layout.addWidget(self.feistelsNet_edit)
        layout.addWidget(self.shannons_t_a_c_edit)
        layout.addWidget(self.magmaKeyInput_edit)
        layout.addWidget(self.magmaVectorInput_edit)
        layout.addWidget(self.A5key_edit)
        layout.addLayout(mode_layout)
        layout.addWidget(self.encrypt_button)

        self.setLayout(layout)
        
        # Переключатель для выбора режима текста
        self.text_mode_checkbox = QCheckBox('Расширенный текст')
        layout.addWidget(self.text_mode_checkbox)

        # Подключение слотов к сигналам
        self.encrypt_button.clicked.connect(self.cipher_parser)
        self.text_mode_checkbox.stateChanged.connect(self.handle_text_mode_change)

    def handle_text_mode_change(self, state):
        if state == Qt.Checked:
            mem["bigTextFlag"] = True
        else:
            mem["bigTextFlag"] = False


    def check_cesar_shift(self):
        shift_text = self.cesar_shift_edit.text()
        try:
            shift = int(shift_text)
            if shift < 0 or shift >= len(alphabet):
                self.cesar_shift_edit.setStyleSheet("QLineEdit { color: red; }")
            else:
                self.cesar_shift_edit.setStyleSheet("")
        except ValueError:
            self.cesar_shift_edit.setStyleSheet("QLineEdit { color: red; }")

    def check_vigener_key(self):
        key_text = self.vigener_key_edit.text()
        if len(key_text) != 1 or key_text.lower() not in alphabet:
            self.vigener_key_edit.setStyleSheet("QLineEdit { color: red; }")
        else:
            self.vigener_key_edit.setStyleSheet("")

    def text_preparation(self, text):
        bigTextFlag = mem["bigTextFlag"]
        if bigTextFlag:
            # Обработка расширенного текста
            return text.replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "прбл").replace(":", "двтч").replace(";", "тчсзп").replace("(", "отскб").replace(")", "зкскб").replace("?", "впрзн").replace("!", "восклзн").replace("\n", "првст").lower()
        else:
            # Обработка обычного текста
            return text.replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "").replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("?", "").replace("!", "").replace("\n", "").lower()


    def cipher_parser(self):
        cipher_choose_input = self.cipher_combo.currentText()
        open_text_input = self.open_text_edit.toPlainText()
        cipher_text_input = self.cipher_text_edit.toPlainText()
        cesar_shift = self.cesar_shift_edit.text()
        keyword = self.keyword_edit.text()
        vigener_keyletter = self.vigener_key_edit.text()
        matrix_input = self.matrix_edit.text()
        cardanosGridSizeInput = self.cardanosGrid_edit.text()
        cardanosGridGRIDInput = self.cardanosGridGRIDGRID_edit.text()
        feistelsNetworkInput = self.feistelsNet_edit.text()
        shannonsNotebookT_A_C = self.shannons_t_a_c_edit.text()
        magmaKeyInput = self.magmaKeyInput_edit.text()
        magmaVectorInput = self.magmaVectorInput_edit.text()
        keyword_A1_A2 = self.A5key_edit.text()

         # Определение режима работы (шифрование или дешифрование)
        mode = 'encrypt' if self.mode_combo.currentText() == 'Шифрование' else 'decrypt'

        # Определение флага для обработки больших текстов
        bigTextFlag = len(open_text_input) > 1000  #ваш порог длины текста

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
                    mode = "encrypt" if self.mode_combo.currentText() == 'Шифрование' else 'decrypt'
                    if mode == "encrypt":
                        cipher_text_input = vigener_encrypt(self.text_preparation(open_text_input), vigener_keyletter, "selfkey", alphabet)
                    elif mode == "decrypt":
                        open_text_input = vigener_decrypt(cipher_text_input, vigener_keyletter, "selfkey", alphabet)
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
        elif cipher_choose_input == "МАГМА(s_block)":
            if mode == "encrypt":
                if s_block_check_parameters(open_text_input, alphabet_sblock):
                    cipher_text_input = s_block_encrypt(open_text_input, alphabet_sblock)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if s_block_check_parameters(cipher_text_input, alphabet_sblock):
                    open_text_input = s_block_decrypt(cipher_text_input, alphabet_sblock)
                else:
                    open_text_input = "Проверьте правильность ввода ключей"
        elif cipher_choose_input == "Шифр Матричный":
            input_matrix = list(map(int, matrix_input.split()))
            matrix_input = [input_matrix[:3], input_matrix[3:6], input_matrix[6:]]
            if matrix_input:
                if matrix_check_parameters(matrix_input):
                    if mode == "encrypt":
                        cipher_text_input = matrix_encrypt(self.text_preparation(open_text_input), matrix_input, alphabet)
                    elif mode == "decrypt":
                        open_text_input = matrix_decrypt(cipher_text_input, matrix_input, alphabet)
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
            keyword = self.keyword_edit.text()
            if keyword:
                if playfair_check_parameters(keyword, alphabet_playfair):
                    if mode == "encrypt":
                        cipher_text_input = playfair_encrypt(self.text_preparation(open_text_input), keyword, alphabet_playfair)
                    elif mode == "decrypt":
                        open_text_input = playfair_decrypt(cipher_text_input, keyword, alphabet_playfair)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ключевого слова"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ключевого слова"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевое слово для шифра Плейфэра"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевое слово для шифра Плейфэра"
        elif cipher_choose_input == "Шифр вертикальной перестановки":
            keyword = self.keyword_edit.text()
            if keyword:
                if vertical_transposition_check_parameters(keyword, alphabet):
                    if mode == "encrypt":
                        cipher_text_input = vertical_transposition_encrypt(self.text_preparation(open_text_input), keyword, alphabet)
                    elif mode == "decrypt":
                         open_text_input = vertical_transposition_decrypt(cipher_text_input, keyword, alphabet)
                else:
                    if mode == "encrypt":
                        cipher_text_input = "Проверьте правильность ключевого слова"
                    elif mode == "decrypt":
                        open_text_input = "Проверьте правильность ключевого слова"
            else:
                if mode == "encrypt":
                    cipher_text_input = "Введите ключевое слово для шифра вертикальной перестановки"
                elif mode == "decrypt":
                    open_text_input = "Введите ключевое слово для шифра вертикальной перестановки"
        elif cipher_choose_input == "Шифр решетка Кардано":
            GridSizeInput = list(map(int, cardanosGridSizeInput.split(" ")))
            GridCardano = [list(map(int, x.split(" "))) for x in cardanosGridGRIDInput.split(", ")]
            if cardanosGridCheckParameters(GridSizeInput, GridCardano):
                if mode == "encrypt":
                    cipher_text_input = cardanosGridEncrypt(self.text_preparation(open_text_input), GridSizeInput, GridCardano, alphabet)
                elif mode == "decrypt":
                    open_text_input = cardanosGridDecrypt(cipher_text_input, GridSizeInput, GridCardano, alphabet)
            else:
                if mode == "encrypt":
                    cipher_text_input = "Проверьте правильность ввода решетки"
                elif mode == "decrypt":
                    open_text_input = "Проверьте правильность ввода решетки"
        elif cipher_choose_input == "Шифр сеть Фейстель":
            if mode == "encrypt":
                if feistelsNetworkCheckParameters(open_text_input, feistelsNetworkInput, alphabet_sblock):
                    cipher_text_input = feistelsNetwork(open_text_input, feistelsNetworkInput, mode, alphabet_sblock)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if feistelsNetworkCheckParameters(cipher_text_input, feistelsNetworkInput, alphabet_sblock):
                    open_text_input = feistelsNetwork(cipher_text_input, feistelsNetworkInput, mode, alphabet_sblock)
                else:
                    open_text_input = "Проверьте правильность ввода ключей"
        elif cipher_choose_input == "Одноразовый блокнот Шеннона":
            if mode == "encrypt":
                if shannonsNotebookCheckParameters(*list(map(int, shannonsNotebookT_A_C.split())), alphabet):
                    cipher_text_input = shannonsNotebookEncrypt(self.text_preparation(open_text_input), *list(map(int, shannonsNotebookT_A_C.split())), alphabet)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if shannonsNotebookCheckParameters(*list(map(int, shannonsNotebookT_A_C.split())), alphabet):
                    open_text_input = shannonsNotebookDecrypt(open_text_input, *list(map(int, shannonsNotebookT_A_C.split())), alphabet)
                else:
                    open_text_input = "Проверьте правильность ввода ключей"
        elif cipher_choose_input == "Hexoize":
            if mode == "encrypt":
                cipher_text_input = StrToHex(open_text_input)
            elif mode == "decrypt":
                open_text_input = HexToStr(cipher_text_input)
        elif cipher_choose_input == "Магма (гаммирование)":
            if mode == "encrypt":
                if MagmaCheckParameters(magmaKeyInput, magmaVectorInput, alphabet_sblock):
                    cipher_text_input = magma(open_text_input, magmaKeyInput, magmaVectorInput, mode, alphabet_sblock)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if MagmaCheckParameters(magmaKeyInput, magmaVectorInput, alphabet_sblock):
                    open_text_input = magma(cipher_text_input, magmaKeyInput, magmaVectorInput, mode, alphabet_sblock)
                else:
                    open_text_input = "Проверьте правильность ввода ключей"
        elif cipher_choose_input == "A5/1":
            if mode == "encrypt":
                if A5CheckParameters(keyword_A1_A2):
                    cipher_text_input = A51(open_text_input, keyword_A1_A2, mode)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if A5CheckParameters(keyword_A1_A2):
                    cipher_text_input = A51(cipher_text_input, keyword_A1_A2, mode)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
        elif cipher_choose_input == "A5/2":
            if mode == "encrypt":
                if A5CheckParameters(keyword_A1_A2):
                    cipher_text_input = A52(open_text_input, keyword_A1_A2, mode)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
            elif mode == "decrypt":
                if A5CheckParameters(keyword_A1_A2):
                    cipher_text_input = A52(cipher_text_input, keyword_A1_A2, mode)
                else:
                    cipher_text_input = "Проверьте правильность ввода ключей"
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
