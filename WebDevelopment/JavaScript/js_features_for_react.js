//https://www.youtube.com/watch?v=m55PTVUrlnA&ab_channel=PedroTech


//1. Arrow functions
//https://www.youtube.com/watch?v=h33Srr5J9nY&t=3s&ab_channel=WebDevSimplified

function sum(a, b) {
    return a + b
} 

function isPositive(a) {
    return a  > 0
} 


function randomNumber() {
    return Math.random()
} 

document.addEventListener('click', function() {
    console.log('Click')
})


console.log(sum(2, 3))
console.log(isPositive(2))
console.log(randomNumber())

let sum2 = ((a, b) => a + b)
console.log(sum2(2, 3))

let isPositive2 = (a) => a > 0
console.log(isPositive2(3))

randomNumber2 = () => Math.random()
console.log(randomNumber2())

document.addEventListener('click', () =>    console.log('Click2'))


//2. Ternary if then statement is
let age1 = 16
let name1 = age1 > 10 ? "Pedro" : "Jack"
console.log(name1)

//3. Destructuring objects and spreading operator
const person = {
    name: "Pedro", 
    age: 20,
    isMarried: false
}

const {name, age, isMarried} = person;
console.log(name, age, isMarried)

const name2 = "Pedro"
const person1 = {
    name2,
    age: 20,
    isMarried: false
}

const person2 = {...person1, name2: "Jack"}
console.log(person2)


const names = ["Pedro", "Jack", "Jessica", "Pedro", "Pedro"]
const names2 = [...names, "Joel"]
console.log(names2)
const names3 = ["Peter", ...names]
console.log(names3)

//4. Manipulating arrays - see array methods
const modifiedNames = names.map((name) => {
    return name + "1"
})
console.log(modifiedNames)

filteredNames = names.filter((name) => {return name != "Pedro"})
console.log(filteredNames)


//4. Async + wait + fetch
