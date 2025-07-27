let button = document.getElementById("button")

let p = document.getElementById("p_tag")

let count = 0

function increase(){
    count++
    p.textContent = count
}

button.addEventListener("click" , increase)



