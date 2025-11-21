let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 10);


let j = 10;
do {
  console.log(j);
  j--;
} while (j >= 1);




let k = 2;
do {
  console.log(k);
  k += 2; 
} while (k <= 20);




let num = 1;
let sum = 0;
do {
  console.log(num);
  sum += num;
  num++;
} while (sum < 100);
console.log("Final sum:", sum);





let m = 1;
do {
  console.log(`5 x ${m} = ${5 * m}`);
  m++;
} while (m <= 10);




let person = {
  name: "Alice",
  age: 25,
  city: "Tbilisi"
};

for (let key in person) {
  console.log(key); 
}



let book = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  year: 1937
};

for (let key in book) {
  console.log(book[key]); 
}




let student = {
  name: "Veron",
  grade: "A",
  age: 16
};

for (let key in student) {
  console.log(key + ": " + student[key]);


}


let car = {
  brand: "Toyota",
  model: "Corolla",
  year: 2020,
  color: "blue",
  mileage: 15000
};

let count = 0;
for (let key in car) {
  count++;
}
console.log("Total properties:", count);

let source = {
  a: 1,
  b: 2,
  c: 3
};

let copy = {};

for (let key in source) {
  copy[key] = source[key];
}

console.log(copy); 
