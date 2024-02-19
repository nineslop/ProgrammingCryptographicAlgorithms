def replace_symbols(text):
    text = text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace("прбл", " ").replace("двтч", ":").replace("тчсзп", ";").replace("отскб", "(").replace("зкскб", ")").replace("впрзн", "?").replace("восклзн", "!").replace("првст", "\n")
    return text

def vertical_transposition_encrypt(text, keyword):
    keyword = ''.join(sorted(keyword))
    num_columns = len(keyword)
    num_rows = -(-len(text) // num_columns)
    num_blanks = num_columns * num_rows - len(text)
    text = replace_symbols(text)
    ciphertext = [''] * num_columns
    col = 0
    row = 0
    for symbol in text:
        ciphertext[col] += symbol
        col += 1
        if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_blanks):
            col = 0
            row += 1
    return ''.join(ciphertext)

def vertical_transposition_decrypt(ciphertext, keyword):
    keyword = ''.join(sorted(keyword))
    num_columns = len(keyword)
    num_rows = -(-len(ciphertext) // num_columns)
    num_blanks = num_columns * num_rows - len(ciphertext)
    plaintext = [''] * num_rows
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[row] += symbol
        col += 1
        if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_blanks):
            col = 0
            row += 1
    plaintext = ''.join(plaintext)
    plaintext = replace_symbols(plaintext)
    return plaintext
