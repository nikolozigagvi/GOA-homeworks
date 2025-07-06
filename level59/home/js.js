number = 123 
console.log(Boolean(123))

bool = true
console.log(String(bool))

str = "456"
console.log(Number(str))

bool = false
console.log(Number(bool))

str2 = "hello"
console.log(Number(str2))

num = prompt("enter you number :")
if (num > 0){
    console.log("you num is possitive")
} else if (num < 0 ){
    console.log("your num is negative")
} else {
    "your num is zero"
}

age = prompt("enter your age :")
if (age => 18){
    console.log("you can vote")
} else {
    console.log("you cany vote")
}

num4 = Number(prompt("enter your num :"))
num3 = Number(prompt("enter your num :"))
if(num4 > num3){
    console.log("the first number is larger than second number")
} else if (num3 > num4){
    console.log("the second number is larger than the first")
} else {
    console.log("both numbers are equal")
}

person = {

}

person.name = "nika"
person.age = 13
person.city = "tbilisi"

console.log(person)