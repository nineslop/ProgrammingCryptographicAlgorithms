import tkinter as tk
from tkinter import ttk

def caesar_cipher(input_str, key):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    punctuations = {
        ",": "зпт",
        ".": "тчк",
        "-": "тире",
    }

    # Заменяем знаки препинания на их "расшифрованные" версии
    for original_char, replacement in punctuations.items():
        input_str = input_str.replace(original_char, replacement)

    result = ""
    for char in input_str:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            index = (alphabet.index(char) + key) % len(alphabet)
            new_char = alphabet[index]

            if not is_upper:
                new_char = new_char.lower()

            result += new_char
        else:
            result += char

    return result

def atbash_cipher(input_str):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    punctuations = {
        ",": "ЗПТ",
        ".": "ТЧК",
        "-": "ТИРЕ",
    }

    preprocessed_input = input_str.upper()
    for char, replacement in punctuations.items():
        preprocessed_input = preprocessed_input.replace(char, replacement)

    result = ""
    for char in preprocessed_input:
        if char in alphabet:
            index = alphabet.index(char)
            result += alphabet[len(alphabet) - index - 1]
        else:
            result += char

    return result

def polybius_square_encrypt(input_str):
    square = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', ',', '.', '-', ' '],
    ]

    input_without_spaces = input_str.replace(' ', '')

    result = ""
    for char in input_without_spaces.upper():
        found = False
        for i in range(len(square)):
            for j in range(len(square[i])):
                if square[i][j] == char:
                    result += f'{i + 1}{j + 1}'
                    found = True
                    break
            if found:
                break
        if not found:
            result += char

    return result

def caesar_decipher(input_str, key):
    return caesar_cipher(input_str, -key)

def atbash_decipher(input_str):
    return atbash_cipher(input_str)

def polybius_square_decrypt(input_str):
    square = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', ',', '.', '-', ' '],
    ]

    decrypted_text = ""
    i = 0
    while i < len(input_str):
        if input_str[i].isdigit() and i + 1 < len(input_str) and input_str[i + 1].isdigit():
            row = int(input_str[i])
            col = int(input_str[i + 1])
            if 1 <= row <= len(square) and 1 <= col <= len(square[row - 1]):
                decrypted_text += square[row - 1][col - 1]
            else:
                decrypted_text += input_str[i:i + 2]
            i += 2
        else:
            decrypted_text += input_str[i]
            i += 1

    return decrypted_text

def extended_cipher(input_str, encryption_dict):
    result = ""
    for char in input_str:
        if char in encryption_dict:
            result += encryption_dict[char]
        else:
            result += char
    return result

def toggle_mode():
    global current_mode
    current_mode = 1 - current_mode  # Toggle between 0 and 1
    mode_label.config(text="Режим: " + ("Обычный" if current_mode == 0 else "Расширенный"))

    global encryption_dict
    if current_mode == 1:
        encryption_dict = {
            ",": "зпт",
            ".": "тчк",
            "-": "тире",
            "!": "вкз",
            "?": "впрз",
            ":": "двтч",
            ";": "тзчк",
            " ": "прбл",
            "\n": "рнрт",
        }
    else:
        encryption_dict = {}  # Reset the dictionary for normal mode

def on_encrypt_button_click():
    text_to_encrypt = input_text.get("1.0", tk.END).strip()
    selected_cipher = cipher_combobox.get()

    if selected_cipher == "Шифр Цезаря":
        key = int(key_entry.get())
        result = caesar_cipher(text_to_encrypt, key)
    elif selected_cipher == "Шифр Атбаш":
        result = atbash_cipher(text_to_encrypt)
    elif selected_cipher == "Квадрат Полибия":
        result = polybius_square_encrypt(text_to_encrypt)
    elif selected_cipher == "Расширенный" and current_mode == 1:
        encryption_dict = {
            ",": "зпт",
            ".": "тчк",
            "-": "тире",
            "!": "вкз",
            "?": "впрз",
            ":": "двтч",
            ";": "тзчк",
            " ": "прбл",
            "\n": "рнрт",
        }
        result = extended_cipher(text_to_encrypt, encryption_dict)
    else:
        result = "Выберите шифр"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def on_decrypt_button_click():
    text_to_decrypt = input_text.get("1.0", tk.END).strip()
    selected_cipher = cipher_combobox.get()

    if selected_cipher == "Шифр Цезаря":
        key = int(key_entry.get())
        result = caesar_decipher(text_to_decrypt, key)
    elif selected_cipher == "Шифр Атбаш":
        result = atbash_decipher(text_to_decrypt)
    elif selected_cipher == "Квадрат Полибия":
        result = polybius_square_decrypt(text_to_decrypt)
    elif selected_cipher == "Расширенный" and current_mode == 1:
        decryption_dict = {
            "зпт": ",",
            "тчк": ".",
            "тире": "-",
            "вкз": "!",
            "впрз": "?",
            "двтч": ":",
            "тзчк": ";",
            "прбл": " ",
            "рнрт": "\n",
        }
        result = extended_cipher(text_to_decrypt, decryption_dict)
    else:
        result = "Выберите шифр"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Создание главного окна
root = tk.Tk()
root.title("Шифры")

# Установка размера окна
root.geometry("640x420")

# Создание и размещение элементов интерфейса
input_label = tk.Label(root, text="Введите текст:")
input_label.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

cipher_label = tk.Label(root, text="Выберите шифр:")
cipher_label.pack()

# Добавляем опцию "Расширенный" в выпадающий список
cipher_combobox = ttk.Combobox(root, values=["Шифр Цезаря", "Шифр Атбаш", "Квадрат Полибия", "Расширенный"])
cipher_combobox.pack()

key_label = tk.Label(root, text="Введите ключ (только для Шифра Цезаря):")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Зашифровать", command=on_encrypt_button_click)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Расшифровать", command=on_decrypt_button_click)
decrypt_button.pack()

# Добавляем кнопку для переключения между режимами
toggle_button = tk.Button(root, text="Переключить режим", command=toggle_mode)
toggle_button.pack()

# Добавляем метку для отображения текущего режима
current_mode = 0  # 0 - Обычный, 1 - Расширенный
mode_label = tk.Label(root, text="Режим: Обычный")
mode_label.pack()

output_label = tk.Label(root, text="Результат:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Запуск основного цикла
root.mainloop()