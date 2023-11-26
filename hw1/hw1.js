// Задача №1
// Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
// сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

const numbers = [];
numbers.push(2, 5, 1, 2, 3);

function sortListImperative(listNumbers) {
    for (let i = 0; i < listNumbers.length; i++) {
        for (let j = 0; j < listNumbers.length; j++) {
          if (listNumbers[j] < listNumbers[j + 1]) {
            let tmp = listNumbers[j];
            listNumbers[j] = listNumbers[j + 1];
            listNumbers[j + 1] = tmp;
          }
        }
      }
    return listNumbers;
}

sortListImperative(numbers);
console.log(numbers)


// Задача №2
// Написать точно такую же процедуру, но в декларативном стиле


const sortListDeclarative = (listNumbers) => listNumbers.sort().reverse();

console.log(sortListDeclarative(numbers));