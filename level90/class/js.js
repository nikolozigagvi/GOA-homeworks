const Mypromice = new Promise((resolve, reject) => {
    setTimeout(() => {
        let mynum = Math.round(Math.random())

        if(mynum === 0){
            resolve("Sucsess")
        } else {
            reject("reject")
        }
    },5000)
})

console.log(Mypromice)