let person = {
    name : "nikoloz",
    surname : "gagvishvili",
    favcolor : "red",
    isgoastudent : true,
    greet : function(){
        console.log("hello")
    }

}

console.log(person)
console.log(person.name)
console.log(greet)

// false
true && false
// false
false && false
// true
true && true
// false
false && true
//true
true || false
//true
true || true
//false
false || false
// true
false || true


let object = {
    name : "names",
    goaloriented : true,
    age : 13,

    fun1 : function(){
        console.log( "hello",this.name)
    },
    fun2 : function(){
        console.log("are you goal oriented " , this.goaloriented)
    },
    fun3 : function(){
        console.log("wow you pretty old" , this.age)
    }

}

console.log(object.fun1)
console.log(object.fun2)
console.log(object.fun3)