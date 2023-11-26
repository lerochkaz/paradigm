// Условие
// На вход подается число n.
// Задача
// Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
// Обоснуйте выбор парадигм.

function printNumber(number) {
    console.log(number);
};

const tableMultiplication = (number, n = 1) => {
    printNumber(number*n);
    if (n !== 9) tableMultiplication(number, ++n);
}

tableMultiplication(7);
