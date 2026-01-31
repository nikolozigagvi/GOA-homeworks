function bool(bool1) {
  return new Promise((resolve, reject) => {
    if (bool1 === false) {
      resolve("suc")
    } else {
      reject("fail")
    }
  })
}

async function Check(){
    let result = await bool(false)
    console.log(result)
}

Check()