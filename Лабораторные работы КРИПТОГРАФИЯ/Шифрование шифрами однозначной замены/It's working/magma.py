from feistelsNetwork import feistelsNetworkCheckParameters, feistelsNetwork

def MagmaCheckParameters(key, init_vector, alphabet):
    for digit in init_vector:
        if not digit.isdigit():
            return False
    for letter in key:
        if letter not in alphabet:
            return False
    return True

def magma(open_text, key, init_vector, mode, alphabet):
    def xor_hex(hex1, hex2):
        binary1 = int(hex1, 16)
        binary2 = int(hex2, 16)
        xor_result = (binary1 ^ binary2).to_bytes((max(binary1.bit_length(), binary2.bit_length()) + 7)// 8, byteorder='big').hex()
        return xor_result
    
    encrypted_text = ""
    init_vector = (init_vector + "0000000000000000")[:16]
    keys = [key[i:i+8] for i in range(0, len(key), 8)]
    rev_keys = keys = keys[::-1]
    keys = keys + keys + keys
    keys = keys + rev_keys

    total =""
    for i in range(0, len(open_text), 16):
        p_i = open_text[i:i+16]
        a0 = init_vector[:8]
        a1 = init_vector[8:16]
        ek = feistelsNetwork(init_vector, key, "encrypt", [])
        c_i = xor_hex(ek, p_i)
        total += c_i
        init_vector = hex(int(init_vector, 16)+ 1)[2:]
    
    encrypted_text = total
    return encrypted_text