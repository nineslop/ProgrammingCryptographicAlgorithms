def belazo_check_parameters(keyword, alphabet):
    if not keyword:
        return False  # Возврат лжи, если ключевое слово не введено
    for keyletter in keyword:
        if keyletter not in alphabet:
            return False  # Возврат лжи, если в ключевом слове присутствуют недопустимые символы
    return True  # Возврат истины, если ключевое слово соответствует требованиям

def belazo_encrypt(open_text, keyword, alphabet):
    encrypted_text = ""  # Шифртекст
    for i in range(len(open_text)):  # Проход по всем символам открытого текста
        element = open_text[i]  # Символ
        encrypted_text += alphabet[(alphabet.index(element) + alphabet.index(keyword[i % len(keyword)])) % len(alphabet)]  # Добавление в итоговый шифртекст зашифрованного символа
    return encrypted_text  # Возврат шифртекста

def belazo_decrypt(encrypted_text, keyword, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    for i in range(len(encrypted_text)):  # Проход по всем символам шифртекста
        element = encrypted_text[i]  # Символ
        decrypted_text += alphabet[(alphabet.index(element) - alphabet.index(keyword[i % len(keyword)]) + len(alphabet)) % len(alphabet)]  # Добавление в итоговый текст расшифрованного символа
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
