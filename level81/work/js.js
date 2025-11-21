function startsWithHello(sentence) {
    return sentence.startsWith("Hello")
}


function filestart(file){
 if(file.startsWith("temp_")){
    return true
 } else{
    return false
 }
}



function deletsthespace(name){
 name.trim("     nikoloz gagvihvili          ")
}


function returntogetspace(trimin){
    trimin = ""

    trimin.trim("")
}




const numbers1 = [3, 7, -2, 5, -8];
const firstNegativeIndex = numbers1.findIndex(num => num < 0);
console.log(firstNegativeIndex); 


const users1 = [
    { name: "Alice", age: 16 },
    { name: "Bob", age: 17 },
    { name: "Charlie", age: 18 }
];
const firstAdultIndex = users1.findIndex(user => user.age >= 18);
console.log(firstAdultIndex);


const numbers2 = [3, -7, 2, -5, 8, -1];
const lastNegativeIndex = numbers2.findLastIndex(num => num < 0);
console.log(lastNegativeIndex); 


const users2 = [
    { name: "Alice", age: 20 },
    { name: "Bob", age: 17 },
    { name: "Charlie", age: 22 },
    { name: "David", age: 16 }
];
const lastAdultIndex = users2.findLastIndex(user => user.age >= 18);
console.log(lastAdultIndex);


const numbers3 = [1, 3, 7, 8, 10];
const firstEven = numbers3.find(num => num % 2 === 0);
console.log(firstEven); 


const products1 = [
    { id: 1, price: 50 },
    { id: 2, price: 150 },
    { id: 3, price: 200 }
];
const firstExpensiveProduct = products1.find(product => product.price > 100);
console.log(firstExpensiveProduct); 


const numbers4 = [1, 3, 4, 7, 10];
const lastEven = numbers4.findLast(num => num % 2 === 0);
console.log(lastEven); 


const products2 = [
    { id: 1, price: 50 },
    { id: 2, price: 150 },
    { id: 3, price: 200 },
    { id: 4, price: 80 }
];
const lastExpensiveProduct = products2.findLast(product => product.price > 100);
console.log(lastExpensiveProduct);

const colors = ["red", "green", "blue", "yellow"];
const blueIndex = colors.indexOf("blue");
console.log(blueIndex); 


const numsWithRepeats = [1, 5, 3, 5, 7];
const firstFiveIndex = numsWithRepeats.indexOf(5);
console.log(firstFiveIndex); 

const fruits = ["banana", "apple", "orange", "apple", "mango"];
const lastAppleIndex = fruits.lastIndexOf("apple");
console.log(lastAppleIndex); 

const numbersWithTens = [10, 5, 10, 7, 10];
const lastTenIndex = numbersWithTens.lastIndexOf(10);
console.log(lastTenIndex); 
