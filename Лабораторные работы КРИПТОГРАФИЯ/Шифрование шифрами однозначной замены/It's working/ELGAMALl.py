from math import gcd, sqrt
from random import choice

def find_coprime(n):
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def fi(n):
    num = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            num += 1
    return num

def comparison(comp):
    for y in range(comp[2]):
        if ((comp[0] * y) % comp[2]) == (comp[1] % comp[2]):
            return y
    return 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def elgamalCheckParameters(p, x, g, y):
    if not (p and x and g and y):
        return False
    if not is_prime(p):
        return False
    if not ((1 < x < p) and (1 < g < p)):
        return False
    if pow(g, x, p) != y:
        return False
    return True

def elgamalEncrypt(open_text, p, x, g, y, alphabet):
    for letter in open_text:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    keys = find_coprime(fi(p))
    encrypted_text = ""
    for letter in open_text:
        ki = choice(keys)
        ai = str(pow(g, ki, p)).zfill(len(str(p)))
        bi = str(pow(y, ki) * alphabet.index(letter) % p).zfill(len(str(p)))
        encrypted_text += ai + bi
    return encrypted_text

def elgamalDecrypt(encrypted_text, p, x, g, y, alphabet):
    len_letter = len(str(p))
    encrypted_text_arr = [encrypted_text[i:i+len_letter*2] for i in range(0, len(encrypted_text), len_letter*2)]
    decrypted_text = ""
    for char in encrypted_text_arr:
        ai, bi = int(char[:len_letter]), int(char[len_letter:])
        decrypted_text += alphabet[comparison([pow(ai, x, p), bi, p])]
    decrypted_text = decrypted_text.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('рвст', '\n')
    return decrypted_text