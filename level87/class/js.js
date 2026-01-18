const student = {
    name: "nikoloz",
    surname: "gagvishvili",
    academy: "GOA",
    favColor: "green",
    favNumber: 6967
};

console.log(manualHasOwn(student, "name"));      //true
console.log(manualHasOwn(student, "myName"));     //   false
console.log(manualHasOwn(student, "favNumber"));  //true
console.log(manualHasOwn(student, "favnumber"));  ///false 



const Obj = {
    name: "nikoloz",
    surname: "gagvishvili",
    age: 67,
    city: "Tbilisi",
    coutry: "Georgia",
    worstcoloroat: "black",
    preferednum: 67,
    hobby: "Football",
    human: true,
    language: "georgian",
};


const keys = Object.keys(Obj)
console.log("Keys:", keys)

const val = Object.values(Obj)
console.log("Values:", val)
