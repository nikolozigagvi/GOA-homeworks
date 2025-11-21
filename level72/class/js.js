const div = document.getElementsByTagName("div")

let leftpos = 0
let toppos = 0

let myint = setInterval(function(){
if(leftpos +=20 , toppos +=20){
    clearInterval(myinterval)
}
div.style.leftpos = div + leftpos + "px"
div.style.toppos = div + toppos + "px"

if (leftpos === 200){
    clearInterval(myinterval)
div.style.height = 300 +"px"
div.style.weight = 300 + "px"
div.style.BackGroundColor = "green"
}

},1500)