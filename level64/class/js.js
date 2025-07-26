//შემოვიტანოთ დივი ჯავაში
let div = document.getElementById("div-main")
// შევქმნათ ფუნქცია რომელიც ქმნის ელემენტს
function elementtodiv(){
    let p = document.createElement("p")
}
// ბოლოს ჩავამატოთ დივში ეს ელემენტი
    div.appendChild(p)

//შემოვიტანოთ სექცია 
let section = document.getElementById("id-1")
//შევქმნათ ფუნქცია რომელიც ქმნის ელემენტს
function nameofthisfunc(){
    let h1 = document.createElement("h1")
}
//სექციიდან წავშალოთ ელემენტი
section.removeChild(h1)
//თვითონ დივიდან წავშალოთ სექცია
div.removeChild(section)