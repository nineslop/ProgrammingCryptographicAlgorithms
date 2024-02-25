from S_block import s_block_encrypt

def addBinary(a, b):
    result = ""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(a[i]) - int('0')
            i -= 1
        if j >= 0:
            sum += int(b[j]) - int('0')
            j -= 1
        result = str(sum % 2) + result
        carry = int(sum / 2)
    if carry > 0:
        result = '1' + result
    return result

def feistelsNetworkCheckParameters(text, key, alphabet):
    if len(text) != 16:
        return False
    if len(key) != 64:
        return False
    for letter in text:
        if letter not in alphabet:
            return False
    for letter in key:
        if letter not in alphabet:
            return False
    return True

def feistelsNetwork(openText, key, mode, alphabet_sblock):
    def hex2bin(hex):
        ans = ""
        for letter in hex:
            ans += bin(int(letter, 16))[2:].zfill(4)
        return ans

    def bin2hex(bin):
        return hex(int(bin, 2))[2:]

    def f(rt, ki):
        sm = format((int(rt, 16) + int(ki, 16)) % (2 ** 32), '08x')
        sBlockOutput = s_block_encrypt(sm, alphabet_sblock)
        shift11 = hex2bin(sBlockOutput)[11:] + hex2bin(sBlockOutput)[:11]
        return shift11

    encryptedText = ""
    keys = [key[i:i+8] for i in range(0, len(key), 8)]
    revKeys = keys[::-1]
    keys = keys + keys + keys
    keys = keys + revKeys
    if mode == "decrypt":
        keys = keys[::-1]

    lt = openText[:8]
    rt = openText[8:]

    for key in keys:
        ff = f(rt, key)
        ltBin = ""
        for i in lt:
            ltBin += hex2bin(i)
        ffXorlt = ""
        for i in range(32):
            ffXorlt += str(int(ff[i]) ^ int(ltBin[i]))

        lt = rt
        rt = format(int(ffXorlt, 2), '08x')

    return rt + lt