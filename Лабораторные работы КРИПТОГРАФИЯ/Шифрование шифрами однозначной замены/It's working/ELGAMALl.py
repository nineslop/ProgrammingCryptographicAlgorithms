# Импорт функций для корректной работы программы.
from random import choice
from functions import encodingFormat, normalText, isPrime, coprime, strToDigits, digitsToStr, inputText, saveOutput



# Функция для генерации трех рандомизаторов
def genNums(n, amnt = 3):
    num = []
    nums = [i for i in range(1, n)]
    while len(num) != amnt:
        m = choice(nums)
        # Проверка на то, что рандомизатор еще не используется и на взаимную простоту рандомизатора и переданного числа (p - 1)
        if m not in num and coprime(m , n):
            num.append(m)
    return num

# Функция для приведя строки к массиву, где длина каждого элемента равна заданной
def groupNums(string, lenght):
    chunks = [string[i - lenght:i] for i in range(lenght, len(string) + 1, lenght)]
    return chunks

# Функция шифрования
def encode(text, p, g, x):
    y = (g**x) % p
    print("Открытые ключи: P = ", p, ", G = ", g, ", Y = ", y)
    print("Закрытый ключ:  X = ", x)
    # Получение трех рандомизаторов
    coprime_nums = genNums(p-1, 3)
    en_text = []
    for i in text:
        # Случайный выбор одного из рандомизаторов
        k = choice(coprime_nums)
        # Вычисление первого числа шифра (g^(k * i) (mod p))
        first_num = str((g ** k) % p).zfill(len(str(p)))
        # Вычисление второго числа шифра (y^(k * i) * Mi (mod p))
        second_num = str(((y ** k) * int(i)) % p).zfill(len(str(p)))
        en_text.extend([first_num, second_num])
    return ''.join(en_text)

# Функция расшифрования
def decode(text, p, x):
    result = []
    text = groupNums(text, 4)
    for i in text:
        # Расшифрование шифротекста
        result.append(str((int(i[2:4]) * (int(i[:2]) ** (p - 1 - x))) % p))
    return result

def testing(text, p=37, g=5, x=5):
    y = (g**x) % p
    print("Открытые ключи: P = ", p, ", G = ", g, ", Y = ", y)
    print("Закрытый ключ:  X = ", x)
    # Получение трех рандомизаторов
    coprime_nums = [25, 11, 17]
    en_text = []
    index = 0
    print("Тест шифрования с k1=25, k2=11, k3=17:\n")
    for i in text:
        # Применение рандомизатора
        k = coprime_nums[index%3]
        index += 1
        # Вычисление первого числа шифра (g^(k * i) (mod p))
        first_num = str((g ** k) % p).zfill(len(str(p)))
        # Вычисление второго числа шифра (y^(k * i) * Mi (mod p))
        second_num = str(((y ** k) * int(i)) % p).zfill(len(str(p)))
        en_text.extend([first_num, second_num])
    result = ''.join(en_text)
    print("Итог:\n")
    print(result)
    print("Расшифрование с теми же параметрами:\n")
    result = groupNums(result, 4)
    arr = []
    for i in result:
        # Расшифрование шифротекста
        arr.append(str((int(i[2:4]) * (int(i[:2]) ** (p - 1 - x))) % p))
    print("Итог:\n")
    print(normalText(digitsToStr(arr)))
    return ''



def main():
    print("Шифр Elgamal")
    action = int(input("Выберите действие:\n 1) Зашифровать\n 2) Расшифровать\n 3) Тестирование\n"))
    # Шифрование.
    if (action == 1):
        text = strToDigits(encodingFormat(inputText()))
        # Ввод параметров.
        while True:
            p = input("Введите большое простое целое число P, больше 32: ")
            if p.isdecimal() and isPrime(int(p)) and (int(p))>=32:
                p = int(p)
                break
            else:
                print("Число ", p, " не является простым или меньше 32")
        while True:
            g = input("Введите большое целое G, при этом G > 1 и G < P: ")
            if g.isdecimal():
                if 1 < int(g) < p:
                    g = int(g)
                    break
                else:
                    print("Число ", g, " не удволетворяет: G > 1 и G < P")
            else:
                print("Число ", g, " не является целым")
        while True:
            x = input("Введите большое целое X, при этом X > 1 и X < P: ")
            if x.isdecimal():
                if 1 < int(x) < p:
                    x = int(x)
                    break
                else:
                    print("Число ", x, " не удволетворяет X > 1 и X < P")
                break
            else:
                print("Число ", x, " не является целым")
        result = encode(text, p, g, x)
        print("Шифротекст:", result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    # Расшифрование.
    elif (action == 2):
        text = inputText()
        # Ввод параметров.
        while True:
            p = input("Введите большое простое целое число P: ")
            if p.isdecimal() and isPrime(int(p)):
                p = int(p)
                break
            else:
                print("Число ", p, " не является простым")
        while True:
            x = input("Введите большое целое X, при этом X > 1 и X < P: ")
            if x.isdecimal():
                if 1 < int(x) < p:
                    x = int(x)
                    break
                else:
                    print("Число ", x, " не удволетворяет X > 1 и X < P")
                break
            else:
                print("Число ", x, " не является целым")
        result = normalText(digitsToStr(decode(text, p, x)))
        print("Текст:", result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    elif (action == 3):
        text = strToDigits(encodingFormat(inputText()))
        testing(text)
    # Ошибочный ввод.
    else:
        print("Некорректный ввод.")
