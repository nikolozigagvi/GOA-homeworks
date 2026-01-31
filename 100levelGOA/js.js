//create an local storage
let classes = JSON.parse(localStorage.getItem("classes"))
let selectedClass = -1 // no class is selected right now

//save classes to the local storge
function save() {
  localStorage.setItem("classes", JSON.stringify(classes))
}

//click to add new goal oriended academy class
function addclass() {
  let newClass = {
    name: "GOA Class " + (classes.length + 1),
    students: []
  }

  classes.push(newClass)
  save()
  showclasses()
}

//display classes as an button
function showclasses() {
  let box = document.getElementById("class")
  box.innerText = ""

  for (let i = 0; i < classes.length; i++) {
    let btn = document.createElement("button")
    btn.innerText = classes[i].name

    btn.onclick = function () {
      selectedClass = i
      document.getElementById("classname").innerText = classes[i].name
      showstudents()
    }

    box.appendChild(btn)
  }
}

//add the student in the selected class
function addingstudent() {
  if (selectedClass === -1) return //no class is selected right now

  let nameInput = document.getElementById("studentname")
  let name = nameInput.value.trim() //remove the spaces

  if (name === "") return //empty imput check

  //add student in the class
  classes[selectedClass].students.push(name)
  save()


  showstudents()

  nameInput.value = ""
}

//show students when you select some class
function showstudents() {
  let list = document.getElementById("studentlist")
  list.innerText = ""

  if (selectedClass === -1) return

  let students = classes[selectedClass].students

  for (let i = 0; i < students.length; i++) {
    let li = document.createElement("li")
    li.innerText = students[i]
    list.appendChild(li)
  }
}


showclasses()
