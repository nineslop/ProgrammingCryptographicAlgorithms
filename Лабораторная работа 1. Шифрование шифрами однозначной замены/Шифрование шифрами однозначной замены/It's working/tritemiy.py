def tritemiy_encrypt(open_text, alphabet):
    encrypted_text = ""  # Шифртекст
    for i in range(len(open_text)):  # Проход по всем символам открытого текста
        element = open_text[i]  # Символ
        encrypted_text += alphabet[(alphabet.index(element) + i) % len(alphabet)]  # Добавление в итоговый шифртекст зашифрованного символа
    return encrypted_text  # Возврат шифртекста

def tritemiy_decrypt(encrypted_text, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    for i in range(len(encrypted_text)):  # Проход по всем символам шифртекста
        element = encrypted_text[i]  # Символ
        decrypted_text += alphabet[(alphabet.index(element) - i % len(alphabet) + len(alphabet)) % len(alphabet)]  # Добавление в итоговый текст расшифрованного символа
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
