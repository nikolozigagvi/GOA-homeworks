let previous = document.getElementById("0")

let next = document.getElementById("1")

let index = 0

let image = document.getElementById("img1")

const images = ["i.webp" , "o.webp" , "r.jpg"]

function slidedshowidk(){
    index = nowindexx
    if(index += image.lenght){
        index = 0
    }
    else if(index < 0){
        nowindexx = image.lenght - 1
    }

    image.src = images[index]
}

previous.addEventListener("click" , function(){
    index--
    slidedshowidk(index)
})

next.addEventListener("click" , function(){
    index++
    slidedshowidk(index)
})

//bubbling - იწყებს ბოლოდან და ამთავრებს დასაწყისში.

//cappturing - იწყებს დასაწყისიდან და ამთავრებს ბოლოში.