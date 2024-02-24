def vertical_transposition_check_parameters(keyword, alphabet):
    for letter in keyword:
        if letter not in alphabet:
            return False  # Буквы ключевого слова отсутствуют в алфавите
    return True

def vertical_transposition_encrypt(open_text, keyword, alphabet):
    for letter in open_text:
        if letter not in alphabet:
            return "Введенный текст содержит запрещенные символы"  # Текстовые буквы не входят в алфавит
    # print("encrypted_text", keyword)
    # print("sorted_keyword", alphabet)
    encrypted_text = ""  # Шифрованный текст
    sorted_keyword = sorted(keyword)
    key = []
    for letter in keyword:  # От ключевого слова к цифровой клавише
        key.append(sorted_keyword.index(letter) + 1)
        sorted_keyword[sorted_keyword.index(letter)] = ""
    cutting_open_text = open_text
    open_text_array = []
    for i in range(len(open_text) // len(keyword)):  # Заполнение матрицы текстом
        open_text_array.append(cutting_open_text[:len(keyword)])
        cutting_open_text = cutting_open_text[len(keyword):]
    open_text_array.append(cutting_open_text)
    print("open_text_array", open_text_array)
    encrypted_text_array = [""] * (len(keyword) + 1)
    for i in range(len(keyword)):  # Заполнение массива путем чтения столбцов
        for row in open_text_array:
            if i < len(row) and row[i]:
                encrypted_text_array[key[i]] += row[i]
    encrypted_text = "".join(encrypted_text_array)
    print("encrypted_text", encrypted_text)
    return encrypted_text  # Возвращение шифрованного текста

def vertical_transposition_decrypt(encrypted_text, keyword, alphabet):
    for letter in encrypted_text:
        if letter not in alphabet:
            return "Введенный текст содержит запрещенные символы"  # Текстовые буквы не входят в алфавит
    decrypted_text = ""  # Расшифрованный текст
    sorted_keyword = sorted(keyword)
    key = []
    for letter in keyword:  # От ключевого слова к цифровой клавише
        key.append(sorted_keyword.index(letter) + 1)
        sorted_keyword[sorted_keyword.index(letter)] = ""
    cutting_encrypted_text = encrypted_text
    encrypted_text_array = [""] * (len(keyword) + 1)
    for i in range(1, len(keyword) + 1):  # Заполнение матрицы текстом
        if key.index(i) < len(encrypted_text) % len(keyword):
            encrypted_text_array[key.index(i)] = cutting_encrypted_text[:len(encrypted_text) // len(keyword) + 1]
            cutting_encrypted_text = cutting_encrypted_text[len(encrypted_text) // len(keyword) + 1:]
        else:
            encrypted_text_array[key.index(i)] = cutting_encrypted_text[:len(encrypted_text) // len(keyword)]
            cutting_encrypted_text = cutting_encrypted_text[len(encrypted_text) // len(keyword):]
    for i in range(len(encrypted_text) // len(keyword) + 1):
        for row in encrypted_text_array:
            if i < len(row) and row[i]:
                decrypted_text += row[i]
    # Перевод символов из текстовых значений в символы
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возвращение расшифрованного текста
