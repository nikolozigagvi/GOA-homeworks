
let num = 6
let powerResult = Math.pow(num, 2)
console.log("Power of 2:", powerResult)


let decimalNumber = 1
let truncatedNumber = Math.trunc(decimalNumber)
console.log("Truncated number:", truncatedNumber)


let smallest = Math.min(4, 9, 2, 7)
console.log("Smallest number:", smallest)

let largest = Math.max(4, 9, 2, 7)
console.log("Largest number:", largest)


let num1 = 4.2
let roundedUp = Math.ceil(num1)
console.log("Rounded up:", roundedUp)


let num2 = 6.01
let nextWhole = Math.ceil(num2)
console.log("Next whole number:", nextWhole)

let num3 = 5.6
let nearest = Math.round(num3)
console.log("Rounded to nearest:", nearest)

if (Math.round(num3) > num3) {
  console.log("The number rounded UP")
} else {
  console.log("The number rounded DOWN")
}

