let str = ""
do{
    str += "nikloz gagvishvili"
}while(str.lenght < 20)
console.log(str)







let num = ""
do{
    num += [1 , 2 , 3 ,4 , 5]
}while(num.length > 5)

for(let char of num){
    console.log(char)
}



let obj ={
    name: "nikoloz",
    age: "13",
    grade: "-99",
}

for(let key in obj){
    console.log(key)
    console.log(obj[key])
}


let i = 1

for(i <= 100 ; i++;){
    if(i % 5 == 0 , i % 7 == 0){
        console.log(i)
    }

}