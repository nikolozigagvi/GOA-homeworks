let count = 0
let mytime = setInterval(() => {
    if(count < 60){
        count++

        let now = new Date
    console.log(now.getSeconds())
    }else{
        clearInterval(mytime)
    }
},1000)