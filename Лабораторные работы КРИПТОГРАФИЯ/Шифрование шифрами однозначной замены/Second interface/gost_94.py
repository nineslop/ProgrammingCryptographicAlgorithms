# Импорт функций, необходимых для корректной работы программы.
from ast import literal_eval
from functions import encodingFormat, isPrime, inputText, saveOutput

# Функция вычисления хэша
def makeHash(text, n, q):
    h = [0]
    for char in text:
        h.append((h[-1] + (ord(char) - 1039))**2 % n)
    if h[-1] % q == 0:
        return 1
    return h[-1]


# Функция для рефакторинга строки перед выполнением программы и ее последующего хэширования
def strToHash(text, n, q):
    result = ''
    result = makeHash(text, n, q)
    if result == 0:
        result = 1
    return result


# Функция проверки параметров
def paramValidation(p = 41, q = 5, a = 16, x = 2):
    if not isPrime(p):
        print('Неверное p, введите еще раз, оно должно быть простым')
        return False
    if not isPrime(q) and (p - 1) % q != 0:
        print('Неверное q, введите еще раз, оно должно быть простым сомножителем p-1')
        return False
    if a <= 1 and a >= (p - 1) and (a ** q) % p != 1:
        print('Неверное а, введите еще раз, оно должно быть таким, что 1 < a < p-1 и (a^q) mod p = 1')
        return False
    if x >= q:
        print('Неверное x, введите еще раз, оно должно быть меньше q')
        return False
    return True


# Функция подписывания
def makeSign(text, p, q, a, x, k, n):
    text = strToHash(encodingFormat(text), n, q)
    # Подсчет первого числа подписи
    # r = (а^k mod p) mod q
    r = ((a ** k) % p) % q
    if r == 0:
        print("Ошибка, r = 0, выберите другое k")
        return "Error"
    # Подстчет второго числа подписи
    # s = (х * r + k (Н(m))) mod q
    s = (x * r + k*text) % q
    y = (a ** x) % p
    print("Открытый ключ Y: ", y)
    r = r % 2**256
    s = s % 2**256
    return [r, s]


# Функция проверки подписи
def checkSign(text, r, s, p, q, a, y, n):
    text = strToHash(text, n, q)
    # Проверка полученной подписи
    #     v = Н(m)q-2 mod q,
    # z1 = (s * v) mod q,
    # z2 = ((q-r) * v) mod q,
    # u = ((а^z1 * у^z2 ) mod р) mod q.
    v = (text ** (q - 2)) % q
    z1 = (s * v) % q
    z2 = ((q - r) * v) % q
    u = ((a ** z1) * (y ** z2)) % p % q
    if u == r:
        res = 'Подпись действительна'
    else:
        res = 'Подпись не действительна.'
    return res



def main():
    print("ЭЦП по ГОСТ Р 34.10-94")
    action = int(input("Выберите действие:\n 1) Подписать\n 2) Проверить\n"))
    # Создание подписи.
    if (action == 1):
        text = inputText()
        # Ввод параметров.
        while True:
            p = int(input("Введите большое простое p: "))
            if isPrime(p) and (int(p))>32:
                break
            else:
                print("Число ", p, " не является простым или меньше 32")
            q = int(input("Введите простое q, являющееся сомножителем числа p-1: "))
            if paramValidation(p, q):
                break
        while True:
            a = int(input("Введите такое а, что 1 < a < p-1 и (a^q) mod p = 1: "))
            x = int(input("Введите x < q: "))
            if  paramValidation(p, q, a, x):
                break
        while True:
            k = int(input("Введите случайное число k, при этом k < q: "))
            if  k >= q:
                print("Неверное k, введите еще раз, оно должно быть меньше q")
            else:
                break
        n = int(input("Введите модуль для хэширования h: "))
        result = makeSign(text, p, q, a, x, k, n)
        print("ЭЦП: " ,result)
        saveOutput(str(result))
        print("Подпись помещена в output.txt")
    # Проверка подписи.
    elif (action == 2):
        text = inputText()
        sign = literal_eval(open('output.txt', 'r',  encoding='UTF8').read())
        r = sign[0]
        s = sign[1]
        # Ввод параметров.
        while True:
            p = int(input("Введите большое простое p: "))
            q = int(input("Введите простое q, являющееся сомножителем числа p-1: "))
            if paramValidation(p, q):
                break
        while True:
            a = int(input("Введите а: "))
            if  paramValidation(p, q, a):
                break
        y = int(input("Введите открытый ключ Y: "))
        n = int(input("Введите модуль для хэширования h: "))
        result = checkSign(text, r, s, p, q, a, y, n)
        print("Результат проверки:", result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    # Ошибочный ввод.
    else:
        print("Некорректный ввод.")
