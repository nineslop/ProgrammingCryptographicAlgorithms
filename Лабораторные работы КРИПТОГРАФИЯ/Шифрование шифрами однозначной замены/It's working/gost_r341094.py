import random

def hash_message(message, mod, alphabet):
    h = 0
    for letter in message:
        h = ((h + alphabet.index(letter) + 1) ** 2) % mod
    return h

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_coprime(n):
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def prime_factors(n):
    factors = []
    divisor = 2
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return factors

def set_y(p, a, x):
    y = pow(a, x, p)
    return y

def set_q(n):
    primes = set(prime_factors(n))
    return primes

def set_k_x_placeholder(q):
    return f"k (1 < k < {q})"

def set_a(p, q):
    as_ = []
    for a in range(2, p - 1):
        if pow(a, q, p) == 1:
            as_.append(a)
    return as_

def gost_r341094_ds_encrypt_check_parameters(p, q, a, x, k):
    if not is_prime(p):
        return "p is not a prime"
    if not q:
        return "Set the parameter q"
    set_k_x_placeholder(q)
    set_a(p, q)
    if not a:
        return "Set the parameter a"
    if not (1 < x < q):
        return "Not 1 < x < q"
    if not (prime_factors(p - 1).count(q)):
        return "q is not a prime multiplier p-1"
    if not ((1 < a) and (a < (p - 1))):
        return "Not 1 < a < p-1"
    if not (((a ** q) % p) == 1):
        return "Not a^q modp = 1"
    set_y(p, a, x)
    if k and not (1 < k < q):
        return "Not 1 < k < q"
    return ""

def gost_r341094_ds_decrypt_check_parameters(p, q, a, y, ds):
    if not all([p, q, a, y]):
        return "p, q, a or y in NaN"
    if not (primes := get_primes(p - 1)).count(q) and (p - 1) % q != 0:
        return "q is not a prime multiplier p-1"
    if not ((1 < a) and (a < (p - 1))):
        return "Not 1 < a < p-1"
    if not (((a ** q) % p) == 1):
        return "Not a^q modp = 1"
    if len(ds.split(" ")) != 2:
        return "Wrong ds length"
    ds_num_arr = [int(x) for x in ds.split(" ")]
    if any(map(lambda x: isinstance(x, str), ds_num_arr)):
        return "Wrong ds"
    return ""

def gost_r341094_ds_encrypt(open_text, p, q, a, x, k=0, alphabet=None):
    if not alphabet:
        return "Alphabet not provided"
    for letter in open_text:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    while (r := pow(a, k, p) % q) == 0:
        if not k:
            k = random.randint(1, q)
        h = hash_message(open_text, len(alphabet), alphabet)
        s = (x * r + k * h) % q
        if h % q == 0:
            h = 1
    return f"{r % (2 ** 256)} {s % (2 ** 256)}"

def gost_r341094_ds_decrypt(open_text, p, q, a, y, ds, alphabet=None):
    if not alphabet:
        return "Alphabet not provided"
    for letter in open_text:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    h = hash_message(open_text, len(alphabet), alphabet)
    v = pow(h, q - 2, q)
    z1 = (ds[1] * v) % q
    z2 = ((q - ds[0]) * v) % q
    u = ((pow(a, z1, p) * pow(y, z2, p)) % p) % q
    if u == ds[0]:
        return "Подпись верна"
    return "Подпись не верна"
