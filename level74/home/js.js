let calculate = (num1 , num2 , operator ) => {
    switch(operator){
        case "+":
        break
            return num1 + num2
        break
        case "-":
            return num1 - num2
        break
        case "*":
            return num1 * num2
        break
        case "/":
            return num1 / num2
        console.log(operator)
        default:
        console.log("no")
        
    }
}


let getinp = (input) => {
    switch(input){
        case "a , e ,i , o ,u":
        break
        return "its is a vowel"
        break
        case "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z":
        break
        return "it is  a consisoant"
        console.log(input)
        default:
        console.log("there is not vowel and consistant")
    }
}



let mounth = (Winter, Spring, Summer, Autumn) => {
    switch(Winter, Spring, Summer, Autumn){
        case "1 ,2 ,3":
        break
        return Winter
        break
        case "4,5,6":
        return Spring
        break
        case "7,8,9":
        break
        return Summer
        break
        case "10,11,12":
        break
        return Autumn
        break
        console.log(mounth)
        default:
        console.log("no mounth")
    }
}





let fruit = (apple, banana, mango) => {
    switch(apple, banana, mango){
    case "5$":
    break
    return apple
    break
    case "3$":
    break
    return banana
    break
    case "67$, tuff":
    break
    return mango
    console.log(fruit)
    default:
    console.log("no tuff fruits seen")

 }}


let num = 7;
let result = (num % 2 === 0) ? "Even" : "Odd";
console.log(result); 


let num2 = -3;
let status = (num2 > 0) ? "Positive"  : (num2 < 0) ? "Negative" : "Zero";
console.log(status); 



let age = 16;
let canVote = (age >= 18) ? "Eligible to vote" : "Not eligible to vote";
console.log(canVote); 


const checkEvenOdd = (n) => (n % 2 === 0 ? "Even" : "Odd");
console.log(checkEvenOdd(8));

