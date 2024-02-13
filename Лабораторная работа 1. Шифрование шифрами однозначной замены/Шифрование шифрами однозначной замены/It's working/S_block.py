def s_block(input_bits):
    """
    Функция принимает на вход биты в виде строки (например, '1010') и применяет S-блок к каждой 4-битовой подпоследовательности.
    Возвращает строку из преобразованных битов.
    """
    sbox = [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]  # Пример S-блока
    output_bits = ""
    for i in range(0, len(input_bits), 4):
        subsequence = input_bits[i:i+4]  # Выделяем 4-битовую подпоследовательность
        decimal_value = int(subsequence, 2)  # Преобразуем её в десятичное число
        substituted_value = sbox[decimal_value]  # Применяем S-блок
        output_bits += format(substituted_value, '04b')  # Преобразуем результат в битовую строку и добавляем к выходной строке
    return output_bits

def combine_s_blocks(outputs):
    """
    Функция принимает на вход словарь выходов S-блоков и объединяет их в одно 32-битное слово.
    Возвращает строку из 32 битов.
    """
    combined_output = ""
    for i in range(8):
        combined_output += outputs[i]  # Просто объединяем выходы каждого S-блока
    return combined_output

def circular_shift_left(bits, shift_amount):
    """
    Функция выполняет циклический сдвиг влево на указанное количество битов.
    """
    return bits[shift_amount:] + bits[:shift_amount]
