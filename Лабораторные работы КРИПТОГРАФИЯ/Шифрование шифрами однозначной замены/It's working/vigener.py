def vigener_check_parameters(key_letter, alphabet):
    if not key_letter:
        return False  # Возврат лжи, если ключевая буква не введена
    if len(key_letter) == 1 and key_letter in alphabet:
        return True  # Возврат истины, если ключевая буква соответствует требованиям
    return False  # Возврат лжи, если в ключевой букве более одного символа или некорректное значение буквы

def vigener_encrypt(open_text, key_letter, mode, alphabet):
    encrypted_text = ""  # Шифртекст
    keyword = key_letter
    for i in range(len(open_text)):  # Проход по всем символам открытого текста
        element = open_text[i]  # Символ
        encrypted_text += alphabet[(alphabet.index(element) + alphabet.index(keyword[i % len(keyword)])) % len(alphabet)]  # Добавление в итоговый шифртекст зашифрованного символа
        if mode == "selfkey":
            keyword += open_text[i]
        elif mode == "cipherkey":
            keyword += encrypted_text[-1]
    return encrypted_text  # Возврат шифртекста

def vigener_decrypt(encrypted_text, key_letter, mode, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    keyword = key_letter
    for i in range(len(encrypted_text)):  # Проход по всем символам шифртекста
        element = encrypted_text[i]  # Символ
        decrypted_text += alphabet[(alphabet.index(element) - alphabet.index(keyword[i % len(keyword)]) + len(alphabet)) % len(alphabet)]  # Добавление в итоговый текст расшифрованного символа
        if mode == "selfkey":
            keyword += decrypted_text[-1]  # добавление к ключу расшифрованной буквы
        elif mode == "cipherkey":
            keyword += encrypted_text[i]
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
