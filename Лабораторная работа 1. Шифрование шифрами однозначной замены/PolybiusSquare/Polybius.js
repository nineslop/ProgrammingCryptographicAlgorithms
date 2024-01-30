function polybiusSquareEncrypt(input) {
    var square = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
        ['М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э'],
        ['Ю', 'Я', '-', ' ', ' ', ' '], // Пробелы добавлены вместо цифр
    ];
    var inputWithoutSpaces = input.replace(/\s/g, ''); // Убираем пробелы из исходного текста
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
var originalText = 'Тот, кто ложится на два стула, падает на ребра.';
var preprocessedText = originalText.replace(/[,.-]/g, function (match) { return match === ',' ? 'зпт' : match === '.' ? 'тчк' : 'тире'; });
var polybiusEncryptedText = polybiusSquareEncrypt(preprocessedText);
console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Зашифрованный текст (Квадрат Полибия):', polybiusEncryptedText);
