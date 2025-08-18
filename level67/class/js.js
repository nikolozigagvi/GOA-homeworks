let button = document.getElementById("prev_butotn")

let button2 = document.getElementById("next_button")

let img = document.getElementById("image")

let images = ["i.jpg " , "i.webp" , "o.webp"  ,"R.jpg"]

let index = 0 

function slide(currindex){
    index = currindex

if(currindex >= images.length){
    index = 0
}else if(currindex < 0 ){
    index = images.length
}
image.src = images[index]

}

previous.addEventListener("click" , function(){
    slide(index - 1)
})

next.addEventListener("click" , function(){
    slide(index + 1)
})

slide()