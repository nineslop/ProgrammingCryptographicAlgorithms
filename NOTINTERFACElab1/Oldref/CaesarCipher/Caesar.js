function caesarCipher(input, key) {
    var alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    var punctuations = {
        ",": "зпт",
        ".": "тчк",
        "-": "тире",
    };
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
var originalText = 'Тот, кто ложится на два стула, падает на ребра.';
var preprocessedText = originalText.replace(/[,.-]/g, function (match) { return match === ',' ? 'зпт' : match === '.' ? 'тчк' : 'тире'; });
var caesarEncryptedText = caesarCipher(preprocessedText, 3);
console.log('Оригинальный текст:', originalText);
console.log('Предварительно обработанный текст:', preprocessedText);
console.log('Шифр Цезаря (с ключом 3):', caesarEncryptedText);
У