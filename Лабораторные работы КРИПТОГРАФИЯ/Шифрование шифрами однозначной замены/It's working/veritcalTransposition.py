def vertical_transposition_check_parameters(keyword, alphabet):
    for letter in keyword:
        if letter not in alphabet:
            return False  # Буквы ключевого слова не содержатся в алфавите
    return True

def vertical_transposition_encrypt(open_text, keyword, alphabet):
    for letter in open_text:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"  # Буквы текста не содержатся в алфавите
    encrypted_text = ""  # Шифртекст
    sorted_keyword = sorted(keyword)
    key = [sorted_keyword.index(letter) + 1 for letter in keyword]  # Из ключевого слова в цифровой ключ
    cutting_open_text = open_text
    open_text_array = [cutting_open_text[i:i + len(keyword)] for i in range(0, len(cutting_open_text), len(keyword))]  # Заполнение матрицы текстом
    encrypted_text_array = [""] * (len(keyword) + 1)
    for i in range(len(keyword)):  # Заполнение массива считыванием по столбцам
        for row in open_text_array:
            if row and len(row) > i:
                encrypted_text_array[key[i] - 1] += row[i]
    encrypted_text = "".join(encrypted_text_array)
    return encrypted_text  # Возврат шифртекста

def vertical_transposition_decrypt(encrypted_text, keyword, alphabet):
    for letter in encrypted_text:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"  # Буквы текста не содержатся в алфавите
    decrypted_text = ""  # Расшифрованный текст
    sorted_keyword = sorted(keyword)
    key = [sorted_keyword.index(letter) + 1 for letter in keyword]  # Из ключевого слова в цифровой ключ
    cutting_encrypted_text = encrypted_text
    encrypted_text_array = [
        cutting_encrypted_text[i:i + (len(encrypted_text) // len(keyword) + (1 if i < len(encrypted_text) % len(keyword) else 0))]]
    for i in range(len(encrypted_text)):  # <-- Fixed the scoping issue here
        for row in encrypted_text_array:
            if row and len(row) > i:
                decrypted_text += row[i]
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзпт', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста

