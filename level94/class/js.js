let apilink = "https://jsonplaceholder.typicode.com/posts"

let ayncfunc = async () =>{
    try{
        let res = await fetch(apilink)
        let res1 = await res.json()
        console.log(res1)

    }catch(error){
        console.log(error)
    }
}

ayncfunc()