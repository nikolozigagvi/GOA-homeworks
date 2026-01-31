
const promice = new Promise((resolve, reject) => {
    let group29 = ["nik , nikz , dan , alex , giro , luka"]
    let randomElement = group29[Math.floor(Math.random() * group29.length)]

    if(randomElement.length < 6){
        reject("no")
    }else{
        resolve("yes")
    }
})

promice
    .then(
        (res) => {
            console.log(res)
    
        },
        (rej) => {
            console.log(rej)
        }
    )