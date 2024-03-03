def StrToHex(s):
    return ''.join(format(ord(c), '03x') for c in s)

def HexToStr(hex_str):
    hex_chunks = [hex_str[i:i+3] for i in range(0, len(hex_str), 3)]
    return ''.join(chr(int(chunk, 16)) for chunk in hex_chunks).replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace("прбл", " ").replace("двтч", ":").replace("тчсзп", ";").replace("отскб", "(").replace("зкскб", ")").replace("впрзн", "?").replace("восклзн", "!").replace("првст", "\n")

