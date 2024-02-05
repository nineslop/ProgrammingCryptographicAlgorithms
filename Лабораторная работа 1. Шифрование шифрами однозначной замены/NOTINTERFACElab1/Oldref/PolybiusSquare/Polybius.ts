function polybiusSquareEncrypt(input: string): string {
    const square: string[][] = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', '-', ' ', ' ', ' '], // Пробелы добавлены вместо цифр
    ];

    const inputWithoutSpaces = input.replace(/\s/g, ''); // Убираем пробелы из исходного текста

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

const originalText = 'Тот, кто ложится на два стула, падает на ребра.';
const preprocessedText = originalText.replace(/[,.-]/g, match => match === ',' ? 'зпт' : match === '.' ? 'тчк' : 'тире');
const polybiusEncryptedText = polybiusSquareEncrypt(preprocessedText);

console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Зашифрованный текст (Квадрат Полибия):', polybiusEncryptedText);
