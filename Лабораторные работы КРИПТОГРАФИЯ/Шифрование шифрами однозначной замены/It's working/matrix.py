def multiply_matrix(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    C = []
    if colsA != rowsB:
        return False
    for i in range(rowsA):
        C.append([])
    for k in range(colsB):
        for i in range(rowsA):
            t = 0
            for j in range(rowsB):
                t += A[i][j] * B[j][k]
            C[i].append(t)
    return C

def determinant(A):
    N = len(A)
    B = [row[:] for row in A]
    denom = 1
    exchanges = 0
    for i in range(N - 1):
        maxN = i
        maxValue = abs(B[i][i])
        for j in range(i + 1, N):
            value = abs(B[j][i])
            if value > maxValue:
                maxN = j
                maxValue = value
        if maxN > i:
            B[i], B[maxN] = B[maxN], B[i]
            exchanges += 1
        else:
            if maxValue == 0:
                return maxValue
        value1 = B[i][i]
        for j in range(i + 1, N):
            value2 = B[j][i]
            B[j][i] = 0
            for k in range(i + 1, N):
                B[j][k] = (B[j][k] * value1 - B[i][k] * value2) / denom
        denom = value1
    if exchanges % 2:
        return -B[N - 1][N - 1]
    else:
        return B[N - 1][N - 1]

def adjugate_matrix(A):
    N = len(A)
    adjA = []
    for i in range(N):
        adjA.append([])
        for j in range(N):
            B = []
            sign = 1 if (i + j) % 2 == 0 else -1
            for m in range(j):
                B.append([A[m][n] for n in range(i)] + [A[m][n] for n in range(i + 1, N)])
            for m in range(j + 1, N):
                B.append([A[m][n] for n in range(i)] + [A[m][n] for n in range(i + 1, N)])
            adjA[i].append(sign * determinant(B))
    return adjA

def inverse_matrix(A):
    det = determinant(A)
    if det == 0:
        return False
    N = len(A)
    B = adjugate_matrix(A)
    for i in range(N):
        for j in range(N):
            B[i][j] /= det
    return B

def matrix_check_parameters(matrix):
    print(matrix)
    if determinant(matrix) == 0:
        return False
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                return False
    if len(matrix) == 3 and len(matrix[2]) == 3:
        return True  # True, если матрица 3х3
    return False  # False, если матрица не соответствует требованиям

def matrix_encrypt(open_text, key_matrix, alphabet):
    encrypted_text = ""
    open_text_array = []
    if len(open_text) % len(key_matrix) != 0:
        open_text += "ф" * (3 - len(open_text) % len(key_matrix))
    for i in range(0, len(open_text), len(key_matrix)):
        vector = []
        for letter in open_text[i:i + len(key_matrix)]:
            vector.append([alphabet.index(letter)])
        open_text_array.append(vector)
    for vector in open_text_array:
        result_matrix = multiply_matrix(key_matrix, vector)
        if not result_matrix:
            break
        for el in result_matrix:
            encrypted_text += "".join(str(e).rjust(3, "0") for e in el)
    return encrypted_text

def matrix_decrypt(encrypted_text, key_matrix, alphabet):
    decrypted_text = ""
    inverse_matrix_ = inverse_matrix(key_matrix)
    encrypted_text_array = []
    for i in range(0, len(encrypted_text), 9):
        vector = []
        current_str = encrypted_text[i:i + 9]
        for j in range(len(key_matrix)):
            vector.append([int(current_str[j * 3:j * 3 + 3])])
        encrypted_text_array.append(vector)
    for vector in encrypted_text_array:
        if not inverse_matrix_:
            break
        result_matrix = multiply_matrix(inverse_matrix_, vector)
        if not result_matrix:
            break
        for el in result_matrix:
            index = int(round(el[0].real)) if isinstance(el[0], complex) else int(round(el[0]))
            if index >= 0:
                decrypted_text += alphabet[index % len(alphabet)]
            else:
                decrypted_text += alphabet[index % len(alphabet)]
    return decrypted_text