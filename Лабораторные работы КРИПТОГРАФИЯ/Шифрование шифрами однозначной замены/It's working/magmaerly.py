from S_block import s_block_encrypt

def addBinary(a: str, b: str) -> str:
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

def magmaErlyCheckParameters(text: str, key: str, alphabet: list) -> bool:
    if len(key) != 64: return False
    for letter in text:
        if letter not in alphabet: return False
    for letter in key:
        if letter not in alphabet: return False
    return True

def magmaerly(openText: str, key: str, mode: str, alphabet_sblock: list) -> str:
    def hex2bin(hex):
        ans = ""
        for letter in hex:
            ans += bin(int(letter, 16))[2:].zfill(4)
        return ans

    def bin2hex(bin):
        return hex(int(bin, 2))[2:]

    def f(rt, ki):
        sm = ("00000000" + hex((int(rt, 16) + int(ki, 16)) % (2 ** 32))[2:])[-8:]
        sBlockOutput = s_block_encrypt(sm, alphabet_sblock)
        shift11 = hex2bin(sBlockOutput)[11:] + hex2bin(sBlockOutput)[:11]
        return shift11

    encryptedText = ""
    keys = [key[i:i+8] for i in range(0, len(key), 8)]
    revKeys = keys[::-1]
    keys = keys * 3 + revKeys
    if mode == "decrypt":
        keys = keys[::-1]
    res = []
    if len(openText) % 16 != 0:
        openText += "ffffffffffffffff"[:(len(openText) % 16) - 16]
    for ltrt in [openText[i:i+16] for i in range(0, len(openText), 16)]:
        lt = ltrt[:8]
        rt = ltrt[8:]
        for key in keys:
            ff = f(rt, key)
            ltBin = "".join([hex2bin(i) for i in lt])
            ffXorlt = "".join([str(int(ff[i]) ^ int(ltBin[i])) for i in range(32)])
            lt = rt
            rt = ("00000000" + bin2hex(ffXorlt))[-8:]
        res.append(rt + lt)
    return "".join(res)


