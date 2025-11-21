function showMessage() {
  let message = "Hello, this is a local variable!";
  console.log(message); // yes
}

showMessage();

console.log(message); //no



function outerFunction() {
  let count = 0
  console.log("Before inner function:", count)

  function innerFunction() {
    count = count + 5
    console.log("Inside inner function:", count)
  }

  innerFunction()
  console.log("After inner function:", count)
}

outerFunction()


function testScope() {
  if (true) {
    var a = "I am var"
    let b = "I am let"
    const c = "I am const"

    console.log(a) //  works
    console.log(b) //  works
    console.log(c) //  works
  }

  console.log(a) //  works 
  console.log(b) //  Error 
  console.log(c) //  Error 
}

testScope()



setInterval(function(){
  console.log("massage")
}, 2000)


let function1 = (num1 , num2) =>{
  i = num1 * num2
  console.log(i)
}