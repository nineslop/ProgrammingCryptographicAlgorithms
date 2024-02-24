import random

def verticalize(GridSizeInput, GridCardano):
    newGrid = []
    for elem in GridCardano:
        newGrid.append([GridSizeInput[0] - elem[0] - 1, elem[1]])
    newGrid.sort()
    return newGrid

def horizontalize(GridSizeInput, GridCardano):
    newGrid = []
    for elem in GridCardano:
        newGrid.append([elem[0], GridSizeInput[1] - elem[1] - 1])
    newGrid.sort()
    return newGrid

def cardanosGridGeneration(GridSizeInput, textLength):
    if GridSizeInput[0] == -1 and GridSizeInput[1] == -1:
        len_ = max(int(textLength ** 0.5), 2)
        GridSizeInput = [len_, len_]
    elif GridSizeInput[0] * GridSizeInput[1] < textLength:
        return [], []
    
    fullGrid = [[i, j] for i in range(GridSizeInput[0]) for j in range(GridSizeInput[1])]
    cardanosGrid = []
    fglen = len(fullGrid) // 4
    
    for _ in range(fglen):
        el1 = random.choice(fullGrid)
        el2 = [el1[0], GridSizeInput[1] - el1[1] - 1]
        el3 = [GridSizeInput[0] - el1[0] - 1, el1[1]]
        el4 = [GridSizeInput[0] - el1[0] - 1, GridSizeInput[1] - el1[1] - 1]
        cardanosGrid.append(el1)
        
        for el in fullGrid[:]:
            if el == el1 or el == el2 or el == el3 or el == el4:
                fullGrid.remove(el)
    
    cardanosGrid.sort(key=lambda x: (x[0], x[1]))
    return [GridSizeInput, cardanosGrid]

def cardanosGridCheckParameters(GridSizeInput, GridCardano):
    def isArrayInArray(arr, item):
        return item in arr
    
    if len(GridSizeInput) != 2 or not all(GridSizeInput):
        return False
    
    if GridSizeInput[0] % 2 != 0 or GridSizeInput[1] % 2 != 0:
        return False
    
    fst = GridCardano
    snd = horizontalize(GridSizeInput, fst)
    trd = verticalize(GridSizeInput, snd)
    fth = horizontalize(GridSizeInput, trd)
    
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

def cardanosGridEncrypt(openText, GridSizeInput, GridCardano, alphabet):
    for letter in openText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    
    encryptedText = ""
    
    if len(openText) < GridSizeInput[0] * GridSizeInput[1]:
        openText = (openText + "заглушка" * ((GridSizeInput[0] * GridSizeInput[1] - len(openText)) // 8 + 1))[:GridSizeInput[0] * GridSizeInput[1]]
    else:
        openText = openText[:GridSizeInput[0] * GridSizeInput[1]]
    
    encryptedTextGrid = [["" for _ in range(GridSizeInput[1])] for _ in range(GridSizeInput[0])]
    
    def fillTextGrid():
        nonlocal cuttedText
        for coord in GridCardano:
            encryptedTextGrid[coord[0]][coord[1]] = cuttedText[0]
            cuttedText = cuttedText[1:]
    
    cuttedText = openText
    fillTextGrid()
    GridCardano = horizontalize(GridSizeInput, GridCardano)
    fillTextGrid()
    GridCardano = verticalize(GridSizeInput, GridCardano)
    fillTextGrid()
    GridCardano = horizontalize(GridSizeInput, GridCardano)
    fillTextGrid()
    
    encryptedText = "".join("".join(row) for row in encryptedTextGrid)
    return encryptedText

def cardanosGridDecrypt(encryptedText, GridSizeInput, GridCardano, alphabet):
    for letter in encryptedText:
        if letter not in alphabet:
            return "Введёный текст содержит запрещённые символы"
    
    decryptedText = ""
    decryptedTextGrid = [[encryptedText[i * GridSizeInput[1] + j] for j in range(GridSizeInput[1])] for i in range(GridSizeInput[0])]
    
    def readTextGrid():
        nonlocal decryptedText
        for coord in GridCardano:
            decryptedText += decryptedTextGrid[coord[0]][coord[1]]
    
    readTextGrid()
    GridCardano = horizontalize(GridSizeInput, GridCardano)
    readTextGrid()
    GridCardano = verticalize(GridSizeInput, GridCardano)
    readTextGrid()
    GridCardano = horizontalize(GridSizeInput, GridCardano)
    readTextGrid()
    
    if "заглушка" in decryptedText:
        decryptedText = decryptedText[:decryptedText.index("заглушка")]
    
    decryptedText = decryptedText.replace("тчк", ".").replace("зпт", ",").replace("тире", "-").replace("прбл", " ").replace("двтч", ":").replace("тчксзпт", ";").replace("отскб", "(").replace("зкскб", ")").replace("впрзн", "?").replace("восклзн", "!").replace("првст", "\n")
    return decryptedText
