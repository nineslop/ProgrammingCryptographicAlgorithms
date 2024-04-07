import math

def hash(message, mod, alphabet):
    h = 0
    for letter in message:
        h = ((h + alphabet.index(letter) + 1) ** 2) % mod
    return h

def setAutocompleteE(es):
    autocomplete_list = [str(e) for e in es]
    return autocomplete_list

def setD(fin, e):
    d = 1
    while (e * d) % fin != 1:
        d += 1
    return d


def gcd(a, b):
    tempA = a
    tempB = b
    while tempB:
        tempA, tempB = tempB, tempA % tempB
    return tempA

def fi(n):
    num = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            num += 1
    return num

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def comparison(comp):
    for y in range(comp[2]):
        if (comp[0] * y) % comp[2] == comp[1] % comp[2]:
            return y
    return 0

def findCoprime(n):
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def RSADSCheckParameters(p, q, e, ds):
    if math.isnan(p) or math.isnan(q):
        return "p or q is NaN"
    if not (isPrime(p) and isPrime(q)):
        return "p or q is not prime"
    if p == q:
        return "p == q"
    if p * q < 32:
        return "p * q < 32"
    if math.isnan(ds):
        return "ds is NaN"
    if not e:
        setAutocompleteE(findCoprime(fi(p * q)))
        return "set the parameter e"
    return setD(fi(p * q), e)

def RSADSEncrypt(openText, p, q, e, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    n = p * q
    h = hash(openText, n, alphabet)
    return str((h ** comparison([e, 1, fi(n)])) % n)

def RSADSDecrypt(openText, p, q, e, ds, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    n = p * q
    h = hash(openText, n, alphabet)
    decriptedHash = ((ds ** e) % n)
    return "Подпись верна" if decriptedHash == h else "Подпись не верна"
