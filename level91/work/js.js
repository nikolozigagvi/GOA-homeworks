const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Data loaded successfully!")
  }, 1000)
})

myPromise
  .then(result => {
    console.log(result)
    
  })
  .catch(error => {
    console.log(error)
    
  })


  const chainPromise = new Promise((resolve) => {
  resolve(5);
});

chainPromise
  .then(num => {
    return num + 5
  })
  .then(num => {
    return num * 2
  })
  .then(num => {
    console.log(num)
  })

  const conditionalPromise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Operation successful!");
  } else {
    reject("Operation failed!");
  }
});

conditionalPromise.then(
  result => {
    console.log(result);
  
  },
  error => {
    console.log(error);
   
  }
);

