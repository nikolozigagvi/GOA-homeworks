const numbers = [-5, -2, 0, -9, 3]

const hasPositive = numbers.some(num => num > 0)

console.log(hasPositive) // true


const words = ["car", "house", "AI", "laptop"]

const shortWordExists = words.some(word => word.length < 4)

console.log(shortWordExists)// true



const nums = [2, 5, 10, 3]

const allPositive = nums.every(n => n > 0)

console.log(allPositive) // true



const users = [
  { age: 20 },
  { age: 25 },
  { age: 18 },
]

const allAdults = users.every(user => user.age >= 18)

console.log(allAdults)// true



const nums2 = [1, 3, 5, 10]

const doubled = nums2.map(n => n * 2)

console.log(doubled) // [2, 6, 10, 20]

