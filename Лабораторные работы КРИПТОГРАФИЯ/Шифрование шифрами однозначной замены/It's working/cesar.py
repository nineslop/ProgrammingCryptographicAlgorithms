def cesar_check_parameters(shift, alphabet):
    if shift <= len(alphabet) - 1:
        return True  # Возврат истины, если сдвиг меньше длины алфавита
    return False  # Возврат лжи, если сдвиг больше длины алфавита

def cesar_encrypt(open_text, shift, alphabet):
    encrypted_text = ""  # Шифртекст
    for i in range(len(open_text)):  # Проход по всем символам открытого текста
        element = open_text[i]  # Символ
        encrypted_text += alphabet[(alphabet.index(element) + shift) % len(alphabet)]  # Добавление в итоговый шифртекст зашифрованного символа
    return encrypted_text  # Возврат шифртекста

def cesar_decrypt(encrypted_text, shift, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    for i in range(len(encrypted_text)):  # Проход по всем символам шифртекста
        element = encrypted_text[i]  # Символ
        decrypted_text += alphabet[(alphabet.index(element) - shift + len(alphabet)) % len(alphabet)]  # Добавление в итоговый текст расшифрованного символа
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
