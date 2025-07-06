let num = 50
console.log(string(num))


let bool = true
console.log(string(bool))

let str = "12"
let num2 = Number(str)
console.log(num2)

let bool2 = true
let num3 = Number(bool2)
console.log(num3)

let usernum = Number(prompt("enter your age :"))
if(usernum >= 0){
    console.log("it is possitive")
} else{
    console.log("its negative")
}
usernum()

let userage = Number(prompt("enter your age :"))
if(userage >= 18){
    console.log("you can vote")
} else{
    console.log("you cant vote")
}


let usernum1 = Number(prompt("enter your num :"))
if (usernum1  % + 1 ){
    console.log("its ლუწი ")
} else{
    console.log ("its კენტი")
}

let object = {
    name:{
        name: "nikloz",
        City : "tbilisi",
        counrty : "georgia",
        money : "lari"
    },
    age:{
        age : 13.2 ,
        year : 2012,
        mounth : "april",
        day : "fifth"
    }

}

object.name.City = "ozurgeti"
object.age.age = 13.3
object.name.money = "dollars"

console.log(object)