// Ciphers.ts

var basicPunctuations: { [key: string]: string } = {
    ",": "зпт",
    ".": "тчк",
    "-": "тире",
};

var extendedPunctuations: { [key: string]: string } = {
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

function caesarCipher(input: string, key: number, useExtendedPunctuations: boolean = false): string {
    const alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    const punctuations = useExtendedPunctuations ? extendedPunctuations : basicPunctuations;
    const preprocessedInput = input
        .toUpperCase()
        .replace(/[,.-]/g, (match) => punctuations[match] || match);
    return preprocessedInput
        .split('')
        .map((char) => {
            if (alphabet.includes(char)) {
                const index = (alphabet.indexOf(char) + key) % alphabet.length;
                return alphabet.charAt(index);
            } else {
                return char;
            }
        })
        .join('');
}

function atbashCipher(input: string, useExtendedPunctuations: boolean = false): string {
    const punctuations = useExtendedPunctuations ? extendedPunctuations : basicPunctuations;
    const alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    const preprocessedInput = input
        .toUpperCase()
        .replace(/[,.\-!?:; \n]/g, (match) => punctuations[match] || match);
    return preprocessedInput
        .split('')
        .map((char) => {
            if (alphabet.includes(char)) {
                const index = alphabet.indexOf(char);
                return alphabet.charAt(alphabet.length - index - 1);
            } else {
                return char;
            }
        })
        .join('');
}

function polybiusSquareEncrypt(input: string): string {
    const square: string[][] = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', '-', ' ', ' ', ' '],
    ];

    const inputWithoutSpaces = input.replace(/\s/g, '');

    return inputWithoutSpaces
        .toUpperCase()
        .split('')
        .map((char) => {
            for (let i = 0; i < square.length; i++) {
                for (let j = 0; j < square[i].length; j++) {
                    if (square[i][j] === char) {
                        return `${i + 1}${j + 1}`;
                    }
                }
            }
            return char;
        })
        .join('');
}
