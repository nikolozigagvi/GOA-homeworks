
//Select a <div> with the id content and use removeChild to remove its first child element.

let div = document.getElementById("content")

let p = document.getElementById("p_child")
p.textContent = "world"

let p2 = document.getElementById("p_child2")
p.textContent = "hello"

function removechild1(){
    div.removeChild(p)
}

//Create a <ul> with three <li> items, then use removeChild to remove the last <li> from the <ul>

let ul = document.getElementById("ul_parrent")

let li = document.getElementById("1_child")

let li2 = document.getElementById("2_child")

let li3 = document.getElementById("3_child")


function removeli(){
    ul.removeChild(li3)
}


//Create a new <p> element and use replaceChild to replace an existing <p> inside a <div> with the id textContainer

let div2 = document.getElementById("new_div")

let  p5 = document.getElementById("new_child")

let p = document.createElement("p")

function replace2(){
    div2.replaceChild(p5 , p)
}

//Use replaceChild to swap out a <button> inside a <div> with a new <span> element.

let div3 = document.getElementById("simon")

let button = document.getElementById("but")

let span = document.createElement('span')

function repleacebut(){
    div3.replaceChild(button , span)
}
