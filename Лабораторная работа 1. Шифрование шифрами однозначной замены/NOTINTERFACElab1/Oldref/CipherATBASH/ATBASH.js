function atbashCipher(input) {
    var alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    var punctuations = {
        ",": "ЗПТ",
        ".": "ТЧК",
        "-": "ТИРЕ",
    };
    var preprocessedInput = input
        .toUpperCase()
        .replace(/[,.-]/g, function (match) { return punctuations[match]; }); // Преобразовываем знаки препинания
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
var originalText = 'Тот, кто ложится на два стула, падает на ребра.';
var preprocessedText = originalText.replace(/[,.-]/g, function (match) { return match === ',' ? 'ЗПТ' : match === '.' ? 'ТЧК' : 'ТИРЕ'; });
var encryptedText = atbashCipher(preprocessedText);
console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Зашифрованный текст:', encryptedText);
