num = 0
console.log(Boolean(num))

num2 = 1 
console.log(Boolean(num2))


str = "hello"
console.log(Boolean(str))

str3 = ""
console.log(Boolean(str3))

null = 'null'
console.log(Boolean("null"))

num7 = Number(prompt("enter your num :"))
if(num7 %2 == 0 ){
    console.log("your number is even")
} else if ( num7 %2 !== 0 ){
    console.log("your num is odd")
}

score = Number(prompt("enter your score :"))
if (score < 100 , score > 90){
    console.log("A")
} else if (score < 89 , score > 80){
    console.log("B")
} else if (score < 79 , score > 70){
    console.log("C")
} else if (score < 69 , score < 60){
    console.log("D")
} else {
    console.log("YOU FAILED")
}