let sec = document.getElementById("section-main")
let button = document.getElementById("but2")
function divadded(){
    let div = document.createElement("div");

    let p = document.createElement("p")
    let ptxt = document.createElement("new div")

    div.appendChild(p)

    div.style.color = "green"
    div.style.background = "blue"

    sec.append(div)
    
}