let div = document.getElementById("id_div")

let down = 0

function aniamtion(){
    down +=100
    div.style.down = down + "px"
    if(down += 400 ){
        clearInterval(interval)
    }


    
}

interval = setInterval(aniamtion , 1000)


// მოვლენა არის გამოწვეული  ხელოვნურად ან ბუნებრივად 