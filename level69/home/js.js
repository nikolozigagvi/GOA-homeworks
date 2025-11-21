let regbtn = document.getElementById("regbtn")
let logbtn = document.getElementById("logbtn")

logbtn.addEventListener("click" , register)
logbtn.addEventListener("click" , login)
// რეგისტრი
function register() {
  let user = document.getElementById("reguser").value;
  let pass = document.getElementById("regpass").value;
// სახელი და პაროლი
  if (user , pass) {
    localStorage.setItem(user, pass); 
    alert("registered successfully!");
  } else {
    alert("please fill all fields.");
  }
}

//შესვლა აქაუნტში
function login() {
  let user = document.getElementById("loguser").value;
  let pass = document.getElementById("logpass").value;

  let storedPass = localStorage.getItem(user);

  if (storedPass === pass) {
  let welcome = document.getElementById("welcome")
  welcome.textContent = "welcome, " + user + "!";
  } else {
    alert("invalid username or password!");
  }
}
