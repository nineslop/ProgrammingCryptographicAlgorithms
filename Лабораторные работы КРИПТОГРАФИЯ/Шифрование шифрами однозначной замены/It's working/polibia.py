def polibia_encrypt(open_text, alphabet):
    encrypted_text = ""  # Шифртекст
    for letter in open_text:  # Проход по всем символам открытого текста
        for i in range(len(alphabet)):  # Проход по строкам алфавита
            row = alphabet[i]  # Строка алфавита
            for j in range(len(row)):  # Проход по символам строки
                if letter == alphabet[i][j]:  # Если зашифровываемая буква совпадает с текущей
                    encrypted_text += f"{i + 1}{j + 1} "  # Добавление в итоговый шифртекст зашифрованного символа
    return encrypted_text  # Возврат шифртекста

def polibia_decrypt(encrypted_text, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    for letter in encrypted_text.split():  # Проход по всем символам шифртекста
        if letter:  # Если буква существует
            row_index = int(letter[0]) - 1
            col_index = int(letter[1]) - 1
            decrypted_text += alphabet[row_index][col_index]  # Добавление в итоговый текст расшифрованного символа
    # Перевод символов из их текстовых значений в символьные
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
