def get_alphabet_index(element, alphabet):
    for row in range(len(alphabet)):
        for col in range(len(alphabet[row])):
            if element == alphabet[row][col]:
                return [row, col]
    return []

def playfair_check_parameters(keyword, alphabet):
    if len(set(keyword)) != len(keyword):
        return False  # Ложь, если буквы в слове не уникальны
    for letter in keyword:
        if letter not in alphabet:
            return False  # Ложь, если буквы в ключевом слове не содержатся в алфавите
    return True  # Истина, если всё ок

def playfair_encrypt(open_text, keyword, alphabet):
    encrypted_text = ""  # Шифртекст
    unprepared_alphabet = list(set(keyword) | set(alphabet))
    new_alphabet = [unprepared_alphabet[i:i+6] for i in range(0, len(unprepared_alphabet), 6)]
    
    for i in range(0, len(open_text) - 1, 2):  # Избавление от биграм из одинаковых букв
        if open_text[i] == open_text[i + 1] and not (open_text[i] == 'ф' and open_text[i + 1] == 'ф'):  # Если биграма не "фф"
            open_text = open_text[:i + 1] + "ф" + open_text[i + 1:]
        elif open_text[i] == open_text[i + 1] and open_text[i] == 'ф' and open_text[i + 1] == 'ф':  # Если биграма "фф"
            open_text = open_text[:i + 1] + "х" + open_text[i + 1:]
    
    open_text += "ф" * (len(open_text) % 2)  # Дополнение строки до чётного кол-ва букв
    
    for i in range(0, len(open_text), 2):  # Зашифрование
        first_index = get_alphabet_index(open_text[i], new_alphabet)
        second_index = get_alphabet_index(open_text[i + 1], new_alphabet)
        if first_index[0] == second_index[0]:
            first_index[1] = (first_index[1] + 1) % 6
            second_index[1] = (second_index[1] + 1) % 6
            encrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
        elif first_index[1] == second_index[1]:
            first_index[0] = (first_index[0] + 1) % 5
            second_index[0] = (second_index[0] + 1) % 5
            encrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
        else:
            first_index[1], second_index[1] = second_index[1], first_index[1]
            encrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
    
    return encrypted_text  # Возврат шифртекста

def playfair_decrypt(encrypted_text, keyword, alphabet):
    decrypted_text = ""  # Расшифрованный текст
    unprepared_alphabet = list(set(keyword) | set(alphabet))
    new_alphabet = [unprepared_alphabet[i:i+6] for i in range(0, len(unprepared_alphabet), 6)]
    
    for i in range(0, len(encrypted_text), 2):  # Зашифрование
        first_index = get_alphabet_index(encrypted_text[i], new_alphabet)
        second_index = get_alphabet_index(encrypted_text[i + 1], new_alphabet)
        if first_index[0] == second_index[0]:
            first_index[1] = (first_index[1] - 1 + 6) % 6
            second_index[1] = (second_index[1] - 1 + 6) % 6
            decrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
        elif first_index[1] == second_index[1]:
            first_index[0] = (first_index[0] - 1 + 5) % 5
            second_index[0] = (second_index[0] - 1 + 5) % 5
            decrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
        else:
            first_index[1], second_index[1] = second_index[1], first_index[1]
            decrypted_text += new_alphabet[first_index[0]][first_index[1]] + new_alphabet[second_index[0]][second_index[1]]
    
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decrypted_text  # Возврат расшифрованного текста
