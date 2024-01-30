function caesarCipher(input: string, key: number): string {
    const alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    const punctuations: { [key: string]: string } = {
        ",": "зпт",
        ".": "тчк",
        "-": "тире",
    };

    const preprocessedInput = input
        .toUpperCase()
        .replace(/[,.-]/g, match => punctuations[match] || match);

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

const originalText = 'Тот, кто ложится на два стула, падает на ребра.';
const preprocessedText = originalText.replace(/[,.-]/g, match => match === ',' ? 'зпт' : match === '.' ? 'тчк' : 'тире');
const caesarEncryptedText = caesarCipher(preprocessedText, 3);

console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Шифр Цезаря (с ключом 3):', caesarEncryptedText);

