function formonac(e){
    e.preventDefault();
    let from = document.getElementById("form1");

    let number = form.elements.number.value
    let text = form.elements.text.value

    console.log(number , text)

    from.reset()
    
}

function changecolor(e){
    e.preventDefault();

let h1 = document.getElementById("h1")
let text = document.getElementById("text")
let color = document.getElementById("color")
h1.textContent = text
h1.style.color = color

form.reset()
}


function checkiftrueotfalseyoudump(){
    let input = document.getElementById("input1")

    console.log(input.checked)
}