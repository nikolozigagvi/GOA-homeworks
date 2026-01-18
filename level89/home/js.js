let mytimeout = setTimeout(() =>{
    console.log("hello")
},2000)


let mytimeout2 = setTimeout(() => {
    let p = document.getElementById("p1").textContent = "hello"
    console.log(p)
},1000)


let mytimeout3 = setTimeout(() => {
    alert("this is a check up")
},3000)


let mytimeout4 = setTimeout(() => {
    console.log("times up!")
},5000);



let user = document.getElementById("user")
let user1 = localStorage.setItem("user")



let username = localStorage.getItem("username");
  if (username) {
    document.getElementById("username").textContent = username;
  } else {
    document.getElementById("username").textContent = "No username found"
  }

  localStorage.removeItem(user1)
  localStorage.clear()

  //JSON.stringify is a function that turns obj into a string
  //JSON.parse is a funtion that turns obj into a number