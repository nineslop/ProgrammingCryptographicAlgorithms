import re

def majority(x1, x2, x3):
    return (x1 and x2) or (x1 and x3) or (x2 and x3)

def text2bin(text):
    return ''.join(format(ord(char), '016b') for char in text)

def bin2text(bin_text):
    return ''.join(chr(int(bin_text[i:i+16], 2)) for i in range(0, len(bin_text), 16))

def A5CheckParameters(key):
    return bool(re.match(r'^[01]{64}$', key))

class LFSR:
    def __init__(self, length, xor_bits, tact_bits=[]):
        self._length = length
        self._xor_bits = xor_bits
        self._tact_bits = tact_bits
        self._lfsr = [0] * length
        self._exit_bit = 0

    @property
    def lfsr(self):
        return self._lfsr

    @lfsr.setter
    def lfsr(self, lfsr):
        self._lfsr = lfsr

    @property
    def tact_bits(self):
        return [self._lfsr[self._length - bit - 1] for bit in self._tact_bits]

    @property
    def exit_bit(self):
        return self._exit_bit

    def bit_filling(self, bit):
        self.tact(bit_filling=bit)

    def tact(self, shift=True, bit_filling=0):
        res_bit = 0
        for xor_bit in self._xor_bits:
            res_bit ^= self._lfsr[self._length - xor_bit - 1]
        self._exit_bit = self._lfsr[0]
        if shift:
            self._lfsr.pop(0)
            self._lfsr.append(res_bit ^ bit_filling)

    def zeroize(self):
        self._lfsr = [0] * self._length

def A51(open_text, key, mode):
    encrypted_text = ""
    R1 = LFSR(19, [13, 16, 17, 18], [8])
    R2 = LFSR(22, [20, 21], [10])
    R3 = LFSR(23, [7, 20, 21, 22], [10])
    bin_text_arr = []
    if mode == "encrypt":
        bin_text_arr = re.findall('.{1,114}', text2bin(open_text))
    elif mode == "decrypt":
        bin_text_arr = re.findall('.{1,114}', open_text)
    for i, bin_text in enumerate(bin_text_arr):
        iter_key = key + format(i, '022b')
        R1.zeroize()
        R2.zeroize()
        R3.zeroize()
        for bit in iter_key:
            R1.bit_filling(int(bit))
            R2.bit_filling(int(bit))
            R3.bit_filling(int(bit))
        for _ in range(100):
            maj = majority(R1.tact_bits[0], R3.tact_bits[0], R2.tact_bits[0])
            R1.tact(R1.tact_bits[0] == maj)
            R2.tact(R2.tact_bits[0] == maj)
            R3.tact(R3.tact_bits[0] == maj)
        for bit in bin_text:
            maj = majority(R1.tact_bits[0], R3.tact_bits[0], R2.tact_bits[0])
            R1.tact(R1.tact_bits[0] == maj)
            R2.tact(R2.tact_bits[0] == maj)
            R3.tact(R3.tact_bits[0] == maj)
            encrypted_text += str(R1.exit_bit ^ R2.exit_bit ^ R3.exit_bit ^ int(bit))
    if mode == "decrypt":
        encrypted_text = bin2text(encrypted_text).replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return encrypted_text


def A52(openText, key, mode):
    encryptedText = ""  # Шифртекст
    R1 = LFSR(19, [13, 16, 17, 18])
    R2 = LFSR(22, [20, 21])
    R3 = LFSR(23, [7, 20, 21, 22])
    R4 = LFSR(17, [11, 16], [3, 7, 10])
    binTextArr = []
    if mode == "encrypt":
        binTextArr = text2bin(openText)
        binTextArr = [binTextArr[i:i+114] for i in range(0, len(binTextArr), 114)]
    elif mode == "decrypt":
        binTextArr = [openText[i:i+114] for i in range(0, len(openText), 114)]
    for i in range(len(binTextArr)):
        ################### Initialization ###################
        # Iteration key
        iterKey = key + ("0000000000000000000000" + bin(i)[2:]).zfill(22)
        # Zeroing registers
        R1.zeroize()
        R2.zeroize()
        R3.zeroize()
        R4.zeroize()
        # Initializing filling of registers
        for bit in iterKey:
            R1.bit_filling(int(bit))
            R2.bit_filling(int(bit))
            R3.bit_filling(int(bit))
            R4.bit_filling(int(bit))
        # Set R4(3) = 1, R4(7) = 1, R4(10) = 1
        R4lfsr = R4.lfsr
        R4lfsr[3] = 1
        R4lfsr[7] = 1
        R4lfsr[10] = 1
        R4.lfsr = R4lfsr
        # First 99 tacts
        for _ in range(100):
            maj = majority(R4.tact_bits[0], R4.tact_bits[1], R4.tact_bits[2])
            if len(R1.tact_bits) >= 4:
                R1.tact(R1.tact_bits[3] == maj)
            if len(R2.tact_bits) >= 2:
                R2.tact(R2.tact_bits[1] == maj)
            if len(R3.tact_bits) >= 3:
                R3.tact(R3.tact_bits[2] == maj)
            R4.tact()
        ################### Encryption ###################
        for binText in binTextArr[i]:
            maj = majority(R4.tact_bits[0], R4.tact_bits[1], R4.tact_bits[2])
            majr1 = majority(R1.lfsr[12], R1.lfsr[14], R1.lfsr[15])
            majr2 = majority(R1.lfsr[9], R1.lfsr[13], R1.lfsr[16])
            majr3 = majority(R1.lfsr[13], R1.lfsr[16], R1.lfsr[18])
            R1.tact(R4.tact_bits[2] == maj)
            R2.tact(R4.tact_bits[0] == maj)
            R3.tact(R4.tact_bits[1] == maj)
            R4.tact()
            encryptedText += str(R1.exit_bit ^ R2.exit_bit ^ R3.exit_bit ^ majr1 ^ majr2 ^ majr3 ^ int(binText))
    # Перевод символов из их текстовых значений в символьные
    if mode == "decrypt":
        encryptedText = bin2text(encryptedText).replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('в��рзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return encryptedText  # Возврат шифртекста


