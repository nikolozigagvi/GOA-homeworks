let num = prompt()

console.log(num)
console.log(typeof num)

let varieble = Number()


console.log(varieble)
console.log(typeof varieble)

function discountFunc(){
   let age = Number()

   if (age < 18){
    console.log("20%")
} else if (age => 18 , age < 65){
    console.log("5%")
} else(console.log("10%"))
}




function compareNums (){
    num1 = Number(prompt("your num:"))
    num2 = Number(prompt("your num:"))

    if (num1 > num2){
        console.log(num1)
    } else if (num1 < num2){
        console.log(num2)
    } else{
        console.log("Numbers are equal")
    }
}
compareNums()
