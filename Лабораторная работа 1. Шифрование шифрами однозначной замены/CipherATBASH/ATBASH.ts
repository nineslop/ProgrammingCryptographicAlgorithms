function atbashCipher(input: string): string {
    const alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    const punctuations: { [key: string]: string } = {
        ",": "ЗПТ",
        ".": "ТЧК",
        "-": "ТИРЕ",
    };

    const preprocessedInput = input
        .toUpperCase()
        .replace(/[,.-]/g, match => punctuations[match]); // Преобразовываем знаки препинания

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

const originalText = 'Тот, кто ложится на два стула, падает на ребра.';
const preprocessedText = originalText.replace(/[,.-]/g, match => match === ',' ? 'ЗПТ' : match === '.' ? 'ТЧК' : 'ТИРЕ');
const encryptedText = atbashCipher(preprocessedText);

console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Зашифрованный текст:', encryptedText);
