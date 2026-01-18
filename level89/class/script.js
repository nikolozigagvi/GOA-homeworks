let masivi = ["breaking bad" , "dexter" ,"spongebob" ]

localStorage.setItem("movies", JSON.stringify(masivi))

let mytimeout = setTimeout(() => {
    let consoledmasivi = localStorage.getItem(movies)
    let consoledmasivi1 = JSON.parse(consoledmasivi)
    console.log(consoledmasivi1)
},2000)