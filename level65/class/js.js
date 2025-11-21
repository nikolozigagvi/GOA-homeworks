let div = document.getElementById("div-main")


let leftpos = 0



function myanimations(){
  leftpos +=100
  div.style.left = leftpos + "px"
  if(leftpos = 600){
    clearInterval("myint")
  }
}
let myint = setInterval(myanimations , 1000)





//შექმენით counter საიტი სადაც უნდა იყოს ერთი ღილაკი და ერთი პარაგრაფი რომლის მნიშვნელობაც იქნება თავიდან 0, შემდეგ როცა ღილაკს დავაჭერთ მნიშვნელობა უნდა გაიზარდოს ერთით




let button = document.getElementById("increase")

let p = document.getElementById("counter")

let num = 0

function increasenum(){
    num ++
    p.style.textContent = num
}