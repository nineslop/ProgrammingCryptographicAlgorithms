import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class DiffieHellmanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Обмен ключами по протоколу Диффи-Хеллмана')
        self.resize(400, 300)
        layout = QVBoxLayout()

        # Метки и поля ввода для входных параметров
        self.n_label = QLabel("n:")
        layout.addWidget(self.n_label)
        self.n_edit = QLineEdit()
        layout.addWidget(self.n_edit)

        self.a_label = QLabel("a:")
        layout.addWidget(self.a_label)
        self.a_edit = QLineEdit()
        layout.addWidget(self.a_edit)

        self.ka_label = QLabel("ka:")
        layout.addWidget(self.ka_label)
        self.ka_edit = QLineEdit()
        layout.addWidget(self.ka_edit)

        self.kb_label = QLabel("kb:")
        layout.addWidget(self.kb_label)
        self.kb_edit = QLineEdit()
        layout.addWidget(self.kb_edit)

        # Кнопка для выполнения обмена ключами по протоколу Диффи-Хеллмана
        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        # Метка для вывода результата
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        # Получение входных параметров
        n = int(self.n_edit.text())
        a = int(self.a_edit.text())
        ka = int(self.ka_edit.text())
        kb = int(self.kb_edit.text())

        # Проверка корректности параметров
        error_message = diffie_hellman_check_parameters(n, a, ka, kb)
        if error_message:
            self.result_label.setText(error_message)
            return

        # Вычисление обмена ключами по протоколу Диффи-Хеллмана
        result = diffie_hellman(n, a, ka, kb)
        self.result_label.setText(result)

def is_prime(num):
    """Проверяет, является ли число простым."""
    # Если число меньше или равно 1, оно не является простым.
    if num <= 1:
        return False
    # Проверяем делится ли число нацело на числа от 2 до квадратного корня из числа.
    for i in range(2, int(num ** 0.5) + 1):
        # Если число делится нацело на любое число от 2 до квадратного корня,
        # оно не является простым.
        if num % i == 0:
            return False
    # Если число прошло через цикл без нахождения делителя,
    # оно является простым.
    return True

def diffie_hellman_check_parameters(n, a, ka, kb):
    """Проверяет, являются ли заданные параметры корректными для обмена ключами по протоколу Диффи-Хеллмана."""
    # Проверяем, чтобы параметр n был задан
    if not n:
        return "Введите значение n"
    # Проверяем, чтобы n был больше 2
    if not (2 < n):
        return "n должно быть больше 2"
    # Проверяем, чтобы n было простым числом
    if not is_prime(n):
        return "n должно быть простым числом"
    # Проверяем, чтобы параметр a был задан
    if not a:
        return "Введите значение a"
    # Проверяем, чтобы a было в допустимых пределах
    if not (1 < a < n):
        return "a должно быть больше 1 и меньше n"
    # Проверяем, чтобы параметр ka был задан
    if not ka:
        return "Введите значение ka"
    # Проверяем, чтобы ka было в допустимых пределах
    if not (1 < ka < n):
        return "ka должно быть больше 1 и меньше n"
    # Проверяем, чтобы параметр kb был задан
    if not kb:
        return "Введите значение kb"
    # Проверяем, чтобы kb было в допустимых пределах
    if not (1 < kb < n):
        return "kb должно быть больше 1 и меньше n"
    # Все параметры корректны, возвращаем None
    return None

def diffie_hellman(n, a, ka, kb):
    """Выполняет обмен ключами по протоколу Диффи-Хеллмана с заданными параметрами."""
    # Вычисляем общие открытые ключи и секретные ключи с использованием заданных параметров
    ya = pow(a, ka, n)  # Вычисляем Ya
    yb = pow(a, kb, n)  # Вычисляем Yb
    xa = pow(yb, ka, n)  # Вычисляем Xa
    xb = pow(ya, kb, n)  # Вычисляем Xb
    # Проверяем, равны ли Xa и Xb, что указывает на корректный обмен ключами
    if xa == xb:
        # Если ключи равны, возвращаем сообщение об успешном обмене ключами
        return f"Открытый ключ Ya = {ya}\nОткрытый ключ Yb = {yb}\nСекретный ключ Xa = {xa}\nСекретный ключ Xb = {xb}\nXa = Xb ({xa} = {xb}) Подпись верна"
    else:
        # Если ключи не равны, возвращаем сообщение о неудаче
        return "Подпись не верна"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiffieHellmanApp()
    ex.show()
    sys.exit(app.exec_())
