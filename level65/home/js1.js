let button = document.getElementById("button1")
let p = document.getElementById("p1")
let button2 = document.getElementById("button2")
let p2 = document.getElementById("p2")

let possnum = 0 
let negnum = 0


function changeammount(){
    possnum++
    negnum--
    p.textContent = possnum
    p2.textContent = negnum

}

