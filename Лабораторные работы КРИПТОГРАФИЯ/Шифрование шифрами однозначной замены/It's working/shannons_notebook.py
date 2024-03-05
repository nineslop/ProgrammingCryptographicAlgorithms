def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def shannonsNotebookCheckParameters(t, a, c, alphabet):
    if not (t and a and c):
        return False # t, a и c не являются числами
    if not (t > 0 and a > 0 and c > 0):
        return False # Числа отрицательные
    if t > 31 or a > 31 or c > 31:
        return False # Числа больше или равны модулю
    if a % 4 != 1:
        return False # a по модулю 4 не равно 1
    if gcd(c, 32) != 1:
        return False # c не соизмеримо с m
    if a <= 1:
        return False
    return True

def shannonsNotebookEncrypt(openText, t, a, c, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы" # Буквы текста не содержатся в алфавите
    encryptedText = "" # Шифртекст
    gamma = [t]
    # Создание гаммы длины openText
    for i in range(len(openText)):
        gamma.append((a * gamma[-1] + c) % len(alphabet))
    # xor гаммы и открытого текста
    for i in range(len(openText)):
        encryptedText += str((alphabet.index(openText[i]) + 1) ^ gamma[i]).zfill(2)[-2:]
    return encryptedText # Возврат шифртекста

def shannonsNotebookDecrypt(encryptedText, t, a, c, alphabet):
    decryptedText = "" # Расшифрованный текст
    gamma = [t]
    # Создание гаммы длины encryptedText / 2
    for i in range(len(encryptedText) // 2):
        gamma.append((a * gamma[-1] + c) % len(alphabet))
    encryptedTextArr = [encryptedText[i:i+2] for i in range(0, len(encryptedText), 2)]
    # Проверка наличия значений для расшифровки
    if not encryptedTextArr:
        return ""
    # xor гаммы и шифртекста
    for i in range(len(encryptedTextArr)):
        try:
            decrypted_char_index = (int(encryptedTextArr[i]) ^ gamma[i]) - 1
            decrypted_char = alphabet[decrypted_char_index % len(alphabet)]
            decryptedText += decrypted_char
        except ValueError:
            # Обработка случая, когда строка не может быть преобразована в целое число
            pass
    decryptedText = decryptedText.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decryptedText # Возврат расшифрованного текста