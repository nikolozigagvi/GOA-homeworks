
let num = 1

switch   (num) {
  case 1:
    console.log("monday");
    break;
  case 2:
    console.log("tuesday");
    break;
  case 3:
    console.log("wednesday");
    break;
  case 4:
    console.log("thursday");
    break;
  case 5:
    console.log("friday");
    break;
  case 6:
    console.log("saturday");
    break;
  case 7:
    console.log("sunday");
    break;
  default:
    console.log("no week day ")
}

let calculate = (num1,num2,operator) =>{
    switch (operator){
        case "+":
           return num1 + num2
        break;
        case "-":
           return num1 - num2
        break;
        case "*":
           return num1 * num2
        break;
        case "/":
            return num1 / num2
        break;
        console.log(operator)
        default:
        console.log("no")
    }

}

function maxnum(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10){
    let max = num1
    for(let num of arguments){
        num > max
        num = max
    }
    return max


}


function funkybuhahaha(str1,str2,str3,str4,str5){
    
    return str1+str2+str3+str4+str5
}



















