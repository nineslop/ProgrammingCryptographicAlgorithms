import random

def verticalize(mk, grid):
    newGrid = []
    for elem in grid:
        newGrid.append([mk[0] - elem[0] - 1, elem[1]])
    newGrid.sort()
    return newGrid

def horizontalize(mk, grid):
    newGrid = []
    for elem in grid:
        newGrid.append([elem[0], mk[1] - elem[1] - 1])
    newGrid.sort()
    return newGrid

def cardanosGridGeneration(mk, textLength):
    if mk[0] == -1 and mk[1] == -1:
        len_ = max(int(textLength ** 0.5), 2)
        mk = [len_, len_]
    elif mk[0] * mk[1] < textLength:
        return [], []
    
    fullGrid = [[i, j] for i in range(mk[0]) for j in range(mk[1])]
    cardanosGrid = []
    fglen = len(fullGrid) // 4
    
    for _ in range(fglen):
        el1 = random.choice(fullGrid)
        el2 = [el1[0], mk[1] - el1[1] - 1]
        el3 = [mk[0] - el1[0] - 1, el1[1]]
        el4 = [mk[0] - el1[0] - 1, mk[1] - el1[1] - 1]
        cardanosGrid.append(el1)
        
        for el in fullGrid[:]:
            if el == el1 or el == el2 or el == el3 or el == el4:
                fullGrid.remove(el)
    
    cardanosGrid.sort(key=lambda x: (x[0], x[1]))
    return [mk, cardanosGrid]

def cardanosGridCheckParameters(mk, grid):
    def isArrayInArray(arr, item):
        return item in arr
    
    if len(mk) != 2 or not all(mk):
        return False
    
    if mk[0] % 2 != 0 or mk[1] % 2 != 0:
        return False
    
    fst = grid
    snd = horizontalize(mk, fst)
    trd = verticalize(mk, snd)
    fth = horizontalize(mk, trd)
    
    for elem in fst:
        if isArrayInArray(snd, elem) or isArrayInArray(trd, elem) or isArrayInArray(fth, elem):
            return False
    
    for elem in snd:
        if isArrayInArray(fst, elem) or isArrayInArray(trd, elem) or isArrayInArray(fth, elem):
            return False
    
    for elem in trd:
        if isArrayInArray(fst, elem) or isArrayInArray(snd, elem) or isArrayInArray(fth, elem):
            return False
    
    for elem in fth:
        if isArrayInArray(fst, elem) or isArrayInArray(snd, elem) or isArrayInArray(trd, elem):
            return False
    
    return True

def cardanosGridEncrypt(openText, mk, grid, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    
    encryptedText = ""
    
    if len(openText) < mk[0] * mk[1]:
        openText = (openText + "заглушка" * ((mk[0] * mk[1] - len(openText)) // 8 + 1))[:mk[0] * mk[1]]
    else:
        openText = openText[:mk[0] * mk[1]]
    
    encryptedTextGrid = [["" for _ in range(mk[1])] for _ in range(mk[0])]
    
    def fillTextGrid():
        nonlocal cuttedText
        for coord in grid:
            encryptedTextGrid[coord[0]][coord[1]] = cuttedText[0]
            cuttedText = cuttedText[1:]
    
    cuttedText = openText
    fillTextGrid()
    grid = horizontalize(mk, grid)
    fillTextGrid()
    grid = verticalize(mk, grid)
    fillTextGrid()
    grid = horizontalize(mk, grid)
    fillTextGrid()
    
    encryptedText = "".join("".join(row) for row in encryptedTextGrid)
    return encryptedText

def cardanosGridDecrypt(encryptedText, mk, grid, alphabet):
    for letter in encryptedText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    
    decryptedText = ""
    decryptedTextGrid = [[encryptedText[i * mk[1] + j] for j in range(mk[1])] for i in range(mk[0])]
    
    def readTextGrid():
        nonlocal decryptedText
        for coord in grid:
            decryptedText += decryptedTextGrid[coord[0]][coord[1]]
    
    readTextGrid()
    grid = horizontalize(mk, grid)
    readTextGrid()
    grid = verticalize(mk, grid)
    readTextGrid()
    grid = horizontalize(mk, grid)
    readTextGrid()
    
    if "заглушка" in decryptedText:
        decryptedText = decryptedText[:decryptedText.index("заглушка")]
    
    decryptedText = decryptedText.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace("прбл", " ").replace("двтч", ":").replace("тчксзпт", ";").replace("отскб", "(").replace("зкскб", ")").replace("впрзн", "?").replace("восклзн", "!").replace("првст", "\n")
    return decryptedText
