// Ciphers.ts
var basicPunctuations = {
    ",": "зпт",
    ".": "тчк",
    "-": "тире",
};
var extendedPunctuations = {
    ",": "зпт",
    ".": "тчк",
    "-": "тире",
    "!": "вкз",
    "?": "впрз",
    ":": "двтч",
    ";": "тзчк",
    " ": "прбл",
    "\n": "рнрт",
};
function caesarCipher(input, key, useExtendedPunctuations) {
    if (useExtendedPunctuations === void 0) { useExtendedPunctuations = false; }
    var alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    var punctuations = useExtendedPunctuations ? extendedPunctuations : basicPunctuations;
    var preprocessedInput = input
        .toUpperCase()
        .replace(/[,.-]/g, function (match) { return punctuations[match] || match; });
    return preprocessedInput
        .split('')
        .map(function (char) {
        if (alphabet.includes(char)) {
            var index = (alphabet.indexOf(char) + key) % alphabet.length;
            return alphabet.charAt(index);
        }
        else {
            return char;
        }
    })
        .join('');
}
function atbashCipher(input, useExtendedPunctuations) {
    if (useExtendedPunctuations === void 0) { useExtendedPunctuations = false; }
    var punctuations = useExtendedPunctuations ? extendedPunctuations : basicPunctuations;
    var alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    var preprocessedInput = input
        .toUpperCase()
        .replace(/[,.\-!?:; \n]/g, function (match) { return punctuations[match] || match; });
    return preprocessedInput
        .split('')
        .map(function (char) {
        if (alphabet.includes(char)) {
            var index = alphabet.indexOf(char);
            return alphabet.charAt(alphabet.length - index - 1);
        }
        else {
            return char;
        }
    })
        .join('');
}
function polybiusSquareEncrypt(input) {
    var square = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', '-', ' ', ' ', ' '],
    ];
    var inputWithoutSpaces = input.replace(/\s/g, '');
    return inputWithoutSpaces
        .toUpperCase()
        .split('')
        .map(function (char) {
        for (var i = 0; i < square.length; i++) {
            for (var j = 0; j < square[i].length; j++) {
                if (square[i][j] === char) {
                    return "".concat(i + 1).concat(j + 1);
                }
            }
        }
        return char;
    })
        .join('');
}
