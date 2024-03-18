import math
from typing import List, Tuple

def gcd(a: int, b: int) -> int:  # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def findCoprime(n: int) -> List[int]:  # Returns the list of n coprimes
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def fi(n: int) -> int:
    num = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            num += 1
    return num

def comparison(comp: List[int]) -> int:  # comp = [x, y, z] xa = ymod(z)
    for y in range(comp[2]):
        if ((comp[0] * y) % comp[2]) == (comp[1] % comp[2]):
            return y
    return 0

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def elgamalCheckParameters(p: int, x: int, g: int, y: int) -> bool:
    if not (p and x and g and y):
        return False  # p, x, g or y is NaN
    if not isPrime(p):
        return False  # p is not a prime
    if not ((1 < x < p) and (1 < g < p)):
        return False  # Not 1 < x < p, 1 < g < p
    if pow(g, x, p) != y:
        return False  # not y ≡ g**x(mod p)
    return True  # Everything is ok

def elgamalEncrypt(openText: str, p: int, x: int, g: int, y: int, alphabet: List[str]) -> str:
    import random
    if any(letter not in alphabet for letter in openText):
        return "Введёный текст содержит запрещённые символы"  # Буквы текста не содержатся в алфавите
    keys = findCoprime(fi(p))
    encryptedText = ""  # Шифртекст
    for letter in openText:
        ki = keys[0]  # Используем первое значение ki из списка
        ai = ("0" * len(str(p)) + str(pow(g, ki, p)))[-len(str(p)):]
        bi = ("0" * len(str(p)) + str((pow(y, ki, p) * alphabet.index(letter)) % p))[-len(str(p)):]
        encryptedText += ai + bi
    return encryptedText  # Возврат шифртекста

def elgamalDecrypt(encryptedText: str, p: int, x: int, g: int, y: int, alphabet: List[str]) -> str:
    lenLetter = len(str(p))
    encryptedTextArr = [(int(encryptedText[i:i+lenLetter]), int(encryptedText[i+lenLetter:i+2*lenLetter])) for i in range(0, len(encryptedText), 2*lenLetter)]
    decryptedText = ""
    for ai, bi in encryptedTextArr:
        decryptedText += alphabet[comparison([pow(ai, x, p), bi, p])]
    # Перевод символов из их текстовых значений в символьые
    decryptedText = decryptedText.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('воскл��н', '!').replace('првст', '\n')
    return decryptedText  # Возврат шифртекста