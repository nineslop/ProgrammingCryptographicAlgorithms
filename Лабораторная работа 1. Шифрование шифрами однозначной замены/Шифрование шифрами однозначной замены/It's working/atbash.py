def atbash_encrypt(open_text, alphabet):
    encrypted_text = ""  # Шифртекст
    for element in open_text:  # Проход по всем символам открытого текста
        encrypted_text += alphabet[len(alphabet) - alphabet.index(element) - 1]  # Добавление в итоговый шифртекст зашифрованного символа
    return encrypted_text  # Возврат шифртекста

def atbash_decrypt(encrypted_text, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    for element in encrypted_text:  # Проход по всем символам шифртекста
        decrypted_text += alphabet[len(alphabet) - alphabet.index(element) - 1]  # Добавление в итоговый текст расшифрованного символа
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста