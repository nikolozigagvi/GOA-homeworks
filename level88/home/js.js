class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    greet() {
        console.log("Hello, my name is " + this.name)
    }
}

const person1 = new Person("nikloz", 20)
person1.greet()


class Car {
    constructor(brand, year) {
        this.brand = brand
        this.year = year
    }

    printBrand() {
        console.log(this.brand)
    }
}

const car1 = new Car("BMW", 2020)
const car2 = new Car("Audi", 2022)

car1.printBrand()
car2.printBrand()


class Animal {
    constructor(type) {
        this.type = type
    }

    printType() {
        console.log(this.type)
    }
}

const animal1 = new Animal("Dog")
animal1.printType()



class Student {
    constructor(name, grade) {
        this.name = name
        this.grade = grade
    }

    printGrade() {
        console.log(this.grade)
    }
}

const student1 = new Student("Nika", 90)
const student2 = new Student("Mari", 85)
const student3 = new Student("Giorgi", 100)

student1.printGrade()
student2.printGrade()
student3.printGrade()


class Book {
    constructor(title, author) {
        this.title = title
        this.author = author
    }

    printTitle() {
        console.log(this.title)
    }
}

const book1 = new Book("1984", "shecsper")
book1.printTitle()
