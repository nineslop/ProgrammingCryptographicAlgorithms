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

def isPrime(num):
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

def RSACheckParameters(n, e, d):
    if not (n and e and d):
        return False
    if d != comparison([e, 1, fi(n)]):
        return False
    if gcd(e, fi(n)) != 1:
        return False
    return True

def RSAEncrypt(openText, n, e, d, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    encryptedText = ""
    for letter in openText:
        block = pow(alphabet.index(letter) + 1, e, n)
        block_str = str(block)
        # Remove leading zeros from the block
        block_str = block_str.lstrip('0')
        # Ensure at least one digit is kept
        if not block_str:
            block_str = '0'
        # Append the block to the encryptedText
        encryptedText += block_str.zfill(len(str(n)))
    print("encryptedText:", encryptedText)
    return encryptedText

def RSADecrypt(encryptedText, n, e, d, alphabet):
    decryptedText = ""
    lenLetter = len(str(n))
    encryptedTextArr = [int(encryptedText[i:i+lenLetter]) for i in range(0, len(encryptedText), lenLetter)]
    for letter in encryptedTextArr:
        decryptedText += alphabet[pow(letter, d, n) - 1]
    decryptedText = decryptedText.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace('прбл', ' ').replace('двтч', ':').replace('тчсзп', ';').replace('отскб', '(').replace('зкскб', ')').replace('впрзн', '?').replace('восклзн', '!').replace('првст', '\n')
    return decryptedText