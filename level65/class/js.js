let div = document.getElementById("div-main")
let div2 = document.getElementById("div-main2")
let div3 = document.getElementById("div-main3")

let leftpos = 0
let downpos = 0
let uppos = 0




function myanimations(){
  leftpos +=100
  div.style.left = leftpos + "px"
  if(leftpos = 600){
    clearInterval("myint")
  }
}

function myanimations(){
  downpospos +=100
  div.style.left = downpos + "px"
  if(downpos = 600){
    clearInterval("myint")
  }
}


function myanimations(){
  uppos +=100
  div.style.left = uppos + "px"
  if(uppos = 600){
    clearInterval("myint")
  }
}



let myint = setInterval(myanimations , 100)





//შექმენით counter საიტი სადაც უნდა იყოს ერთი ღილაკი და ერთი პარაგრაფი რომლის მნიშვნელობაც იქნება თავიდან 0, შემდეგ როცა ღილაკს დავაჭერთ მნიშვნელობა უნდა გაიზარდოს ერთით




let button = document.getElementById("increase")

let p = document.getElementById("counter")

let num = 0

function increasenum(){
    num ++
    p.style.textContent = num
}