def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def shannons_notebook_check_parameters(t, a, c, alphabet):
    if not (t and a and c):
        return False  # t, a, and c are not numbers
    if not (t > 0 and a > 0 and c > 0):
        return False  # Numbers are negative
    if t > 31 or a > 31 or c > 31:
        return False  # Numbers are greater than or equal to the modulus
    if a % 4 != 1:
        return False  # a modulo 4 is not equal to 1
    if gcd(c, 32) != 1:
        return False  # c is not coprime with m
    return True


def shannons_notebook_encrypt(open_text, t:int, a:int, c:int, alphabet):
    for letter in open_text:
        if letter not in alphabet:
            print("alphabet", alphabet)
            print("t", t)
            print("a", a)
            print("c", c)
            print("open_text", open_text)
            return "Введёный текст содержит запрещённые символы"  # Буквы в тексте не входят в алфавит
    encrypted_text = ""  # Зашифрованный текст
    gamma = [t]
    # Создание гаммы длины open_text
    for i in range(len(open_text)):
        gamma.append((a * gamma[-1] + c) % len(alphabet))
    # XOR гамма и открытый текст
    for i in range(len(open_text)):
        encrypted_text += format((alphabet.index(open_text[i]) + 1) ^ gamma[i], '02x')
    return encrypted_text  # Возвращение зашифрованного текста

def shannons_notebook_decrypt(encrypted_text, t, a, c, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    gamma = [t]
    # Создание гаммы длины encrypted_text // 2
    for i in range(len(encrypted_text) // 2):
        gamma.append((a * gamma[-1] + c) % len(alphabet))
    encrypted_text_arr = [encrypted_text[i:i+2] for i in range(0, len(encrypted_text), 2)]
    if not encrypted_text_arr:
        return ""
    # XOR гамма и зашифрованный текст
    for i in range(len(encrypted_text_arr)):
        decrypted_text += alphabet[((int(encrypted_text_arr[i], 16) ^ gamma[i]) - 1) % len(alphabet)]
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace("прбл", " ").replace("двтч", ":").replace("тчсзп", ";").replace("отскб", "(").replace("зкскб", ")").replace("впрзн", "?").replace("восклзн", "!").replace("првст", "\n")
    return decrypted_text  # Возвращение расшифрованного текста
