import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fi(n):
    num = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            num += 1
    return num

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def comparison(comp):
    for y in range(comp[2]):
        if ((comp[0] * y) % comp[2]) == (comp[1] % comp[2]):
            return y
    return 0

def find_coprime(n):
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def rsa_check_parameters(p, q, e, d):
    if not (p and q):
        return "p or q is NaN"
    if not (is_prime(p) and is_prime(q)):
        return "p or q is not prime"
    if p == q:
        return "p == q"
    if p * q < 32:
        return "p * q < 32"
    if not e:
        return "set the parameter e"
    # The above commented lines are related to web-specific functionality and are not directly translatable to Python.

def rsa_encrypt(open_text, p, q, e, alphabet):
    if any(letter not in alphabet for letter in open_text):
        return "Введёный текст содержит запрещённые символы"
    n = p * q
    encrypted_text = ""
    for letter in open_text:
        encrypted_text += ("0" * len(str(n)) + str(pow(int(alphabet.index(letter) + 1), e, n))).zfill(len(str(n)))
    return encrypted_text

def rsa_decrypt(encrypted_text, p, q, e, d, alphabet):
    decrypted_text = ""
    n = p * q
    len_letter = len(str(n))
    encrypted_text_arr = [int(encrypted_text[i:i+len_letter]) for i in range(0, len(encrypted_text), len_letter)]
    for letter in encrypted_text_arr:
        decrypted_text += alphabet[pow(letter, d, n) - 1]
    # The replacement of specific substrings with characters is a specific requirement that can be handled as follows:
    replacements = {
        "тчк": ".", "зпт": ",", "тире": "-", "прбл": " ", "двтч": ":", "тчсзп": ";",
        "отскб": "(", "зкск": ")", "впрзн": "?", "восклзн": "!", "првст": "\n"
    }
    for key, value in replacements.items():
        decrypted_text = decrypted_text.replace(key, value)
    return decrypted_text


