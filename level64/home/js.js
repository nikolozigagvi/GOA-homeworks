//cloneNode,createElement,appendChild,replaceChild)
//cloneNode - clones the element we put in cloneNode
//createElement - creates element in java script 
//appendChild - adds child element to parent element
//replaceChild - repleaces child elements
//removeChild - removes child element in parrent element


let button = document.getElementById("button1")

button.style.color = "green"
button.style.backgroundColor = "red"
button.textContent = "click me for free code:)))))))))))))"

function changebut(){
    p = document.createElement("p")
    p.textContent = "hello my name is nikoloz gagvishvili"
    button.appendChild(p)
}

let div = document.getElementById("div_main")
let section = document.getElementById("section")

div.appendChild(button)
div.appendChild(section)

div.replaceChild(section  , button)


div.removeChild(button)
