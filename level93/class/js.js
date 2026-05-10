function returnPromise(){
    return new Promise((resolve, reject) => {
        let randommath = Math.random()

        if(randommath < 0.5){
            reject("rej")
        }else{
            resolve("res")
        }
    })

}


let asyncfunc = async () => {
    try{
        let res =  await Promise.all[returnPromise(),returnPromise(),returnPromise()]
        console.log(res)
    } catch (error){
        console.log(error)

    }
    

    }