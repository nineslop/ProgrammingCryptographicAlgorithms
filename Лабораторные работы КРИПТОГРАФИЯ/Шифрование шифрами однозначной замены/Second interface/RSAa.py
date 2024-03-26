# Импорт функций, необходимых для корректной работы программы.
from textwrap import wrap
from functions import encodingFormat, normalText, isPrime, coprime, strToDigits, digitsToStr, inputText, saveOutput

# Расширенный алгоритм Евклида
def invMOD(e, f):
    if e == 0:
        return (f, 0, 1)
    else:
        g, y, x = invMOD(f % e, e)
    return (g, x - (f // e) * y, y)

# Использование расширенного алгоритма Евклида для поиска d из сравнения ed ≡ 1(modf(n))
def invMODres(e, f):
    g, x, y = invMOD(e, f)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % f

# Функция шифрования
def encode(text, e, n):
    result = ''
    for i in text:
        result += str((int(i) ** e) % n).zfill(len(str(n)))
    return result

# Функция расшифрования
def decode(text, d, n):
    text = wrap(text, (len(str(n))))
    for i in range(len(text)):
        text[i] = (int(text[i]) ** d) % n
    return text

def check_e_d(e, d):
    if e == d:
        return False  # e равно d
    else:
        return True   # e не равно d

def main():
    print("RSA")
    action = int(input("Выберите действие:\n 1) Зашифровать\n 2) Расшифровать\n"))
    # Шифрование.
    if (action == 1):
        text = strToDigits(encodingFormat(inputText()))
        while True:
            p = int(input("Введите простое число p: "))
            if isPrime(p):
                break
            else:
                print('Неверное p, оно должно быть простым')
        while True:
            q = int(input("Введите простое число q: "))
            if isPrime(q):
                break
            else:
                print('Неверное q, оно должно быть простым')
        
        while p * q < 32:  # Добавленный цикл проверки условия.
            print("p * q < 32. Пожалуйста, введите значения p и q снова.")
            while True:
                p = int(input("Введите простое число p: "))
                if isPrime(p):
                    break
                else:
                    print('Неверное p, оно должно быть простым')
            while True:
                q = int(input("Введите простое число q: "))
                if isPrime(q):
                    break
                else:
                    print('Неверное q, оно должно быть простым')

        n = p * q
        print("n: ", n)
        f = (p-1)*(q-1) # ф-я Эйлера.
        print("f: ", f)
        while True:
            e = int(input("Введите случайное целое число e, взаимно простое с f: "))
            if coprime(e, f):
                break
            else:
                print('Неверное e, оно должно быть взаимно простым с f')
        
        d = invMODres(e, f)
        print("d: ", d)
        
        while e == d:
            print("Не правильный ввод. e не может быть равен d.")
            e = int(input("Введите случайное целое число e, взаимно простое с f: "))
            d = invMODres(e, f)
            print("d: ", d)
        
        result = encode(text, e, n)
        print("Шифротекст:", result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    # Расшифрование.
    elif (action == 2):
        text = inputText()
        d = int(input("Введите d: "))
        n = int(input("Введите n: "))
        result = normalText(digitsToStr(decode(text, d, n)))
        print("Текст:", result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    # Ошибочный ввод.
    else:
        print("Некорректный ввод.")
