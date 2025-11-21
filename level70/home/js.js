let counter = 1
let myint = setInterval(function(){
    counter++
    console.log(counter)



    if(counter === 5){
        clearInterval(myint)
    }
    
},500)




myarr = [1, "nika" , 49 , 66 , 67]

console.log(myarr[2])

myarr[2] = "nikas"

console.log(myarr)


numofarr = [1,2,3,4,5]

num = numofarr[0] + numofarr[4]

console.log(num)