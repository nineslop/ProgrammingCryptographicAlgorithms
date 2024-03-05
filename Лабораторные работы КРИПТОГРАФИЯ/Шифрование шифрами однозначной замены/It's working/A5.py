import re

class LFSR:
    def __init__(self, length, xorBits, tactBits = []):
        self._length = length
        self._xorBits = xorBits
        self._tactBits = tactBits
        self._lfsr = [0] * length
        self._exitBit = 0

    @property
    def lfsr(self):
        return self._lfsr

    @lfsr.setter
    def lfsr(self, lfsr):
        self._lfsr = lfsr

    @property
    def tactBits(self):
        tactBitValues = []
        for tactBit in self._tactBits:
            tactBitValues.append(self._lfsr[self._length - tactBit - 1])
        return tactBitValues

    @property
    def exitBit(self):
        return self._exitBit

    def bitFilling(self, bit):
        self.tact(bit)

    def tact(self, shift=True, bitFilling=0):
        resBit = 0
        for xorBit in self._xorBits:
            resBit = self._lfsr[self._length - xorBit - 1] ^ resBit
        self._exitBit = self._lfsr[0]
        if shift:
            self._lfsr.pop(0)
            self._lfsr.append(resBit ^ bitFilling)

    def zeroize(self):
        self._lfsr = [0] * self._length

def majority(x1, x2, x3):
    return x1 and x2 or x1 and x3 or x2 and x3

def text2bin(text):
    return ''.join(format(ord(char), '016b') for char in text)

def bin2text(binText):
    text = ""
    for i in range(0, len(binText), 16):
        bin = binText[i:i+16]
        text += chr(int(bin, 2))
    return text

def A5CheckParameters(key):
    return bool(re.match(r'[0,1]{64}', key)) and len(key) == 64

def A51(openText, key, mode):
    encryptedText = ""
    R1 = LFSR(19, [13, 16, 17, 18], [8])
    R2 = LFSR(22, [20, 21], [10])
    R3 = LFSR(23, [7, 20, 21, 22], [10])
    binTextArr = []
    if mode == "encrypt":
        binTextArr = re.findall(r'.{1,114}', text2bin(openText))
    elif mode == "decrypt":
        binTextArr = re.findall(r'.{1,114}', openText)
    for i in range(len(binTextArr)):
        iterKey = key + ("0000000000000000000000" + bin(i)[2:]).zfill(22)
        R1.zeroize()
        R2.zeroize()
        R3.zeroize()
        for bit in iterKey:
            R1.bitFilling(int(bit))
            R2.bitFilling(int(bit))
            R3.bitFilling(int(bit))
        for _ in range(100):
            maj = majority(R1.tactBits[0], R3.tactBits[0], R2.tactBits[0])
            R1.tact(R1.tactBits[0] == maj)
            R2.tact(R2.tactBits[0] == maj)
            R3.tact(R3.tactBits[0] == maj)
        for binText in binTextArr[i]:
            maj = majority(R1.tactBits[0], R3.tactBits[0], R2.tactBits[0])
            R1.tact(R1.tactBits[0] == maj)
            R2.tact(R2.tactBits[0] == maj)
            R3.tact(R3.tactBits[0] == maj)
            encryptedText += str(R1.exitBit ^ R2.exitBit ^ R3.exitBit ^ int(binText))
    if mode == "decrypt":
        encryptedText = bin2text(encryptedText).replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return encryptedText

def A52(openText, key, mode):
    encryptedText = ""
    R1 = LFSR(19, [13, 16, 17, 18])
    R2 = LFSR(22, [20, 21], [10])  # Инициализация TactBits для R2
    R3 = LFSR(23, [7, 20, 21, 22], [10])  # Инициализацию TactBits для R3
    R4 = LFSR(17, [11, 16], [3, 7, 10])
    binTextArr = []
    if mode == "encrypt":
        binTextArr = re.findall(r'.{1,114}', text2bin(openText))
    elif mode == "decrypt":
        binTextArr = re.findall(r'.{1,114}', openText)
    for i in range(len(binTextArr)):
        iterKey = key + ("0000000000000000000000" + bin(i)[2:]).zfill(22)
        R1.zeroize()
        R2.zeroize()
        R3.zeroize()
        R4.zeroize()
        for bit in iterKey:
            R1.bitFilling(int(bit))
            R2.bitFilling(int(bit))
            R3.bitFilling(int(bit))
            R4.bitFilling(int(bit))
        R4lfsr = R4.lfsr
        R4lfsr[3] = 1
        R4lfsr[7] = 1
        R4lfsr[10] = 1
        R4.lfsr = R4lfsr
        for _ in range(99):
            maj = majority(R4.tactBits[0], R4.tactBits[1], R4.tactBits[2])
            R1.tact(R4.tactBits[2] == maj)
            R2.tact(R2.tactBits[0] == maj)
            R3.tact(R3.tactBits[0] == maj)
            R4.tact()
        for binText in binTextArr[i]:
            maj = majority(R4.tactBits[0], R4.tactBits[1], R4.tactBits[2])
            majr1 = majority(R1.lfsr[12], R1.lfsr[14], R1.lfsr[15])
            majr2 = majority(R1.lfsr[9], R1.lfsr[13], R1.lfsr[16])
            majr3 = majority(R1.lfsr[13], R1.lfsr[16], R1.lfsr[18])
            R1.tact(R4.tactBits[2] == maj)
            R2.tact(R4.tactBits[0] == maj)
            R3.tact(R4.tactBits[1] == maj)
            R4.tact()
            encryptedText += str(R1.exitBit ^ R2.exitBit ^ R3.exitBit ^ majr1 ^ majr2 ^ majr3 ^ int(binText))
    if mode == "decrypt":
        encryptedText = bin2text(encryptedText).replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return encryptedText