//https://www.youtube.com/watch?v=NIq3qLaHCIs&ab_channel=WebDevSimplified

//console.log("Hello World!");
const num = [1, 2, 3, 4, 5];
const alpha = ["a", "b", "c", "d", "e"];

//const a = num[0]
//const b = num[1]

// const [a, b] = num;
// console.log(a);
// console.log(b);

//const [a, , b] = num;
//console.log(a);
//console.log(b);

// const [a, , b, ...rest] = num;
// console.log(a);
// console.log(b);
// console.log(rest)

// const newArray = [...num, ...alpha];
// console.log(newArray);

 function sumAndMult(a, b) {
   return [a + b, a * b, a/b];
 }
 // const arr = sumAndMult(2, 3);
 // console.log(arr);

// [s, m, div="No division"] = sumAndMult(2, 3);
// console.log(s);
// console.log(m);
// console.log(div)

// const con = [0, ...num]
// console.log(con)

const person1 = {
  name: 'Kyle',
  age: 24,
  address: {
    city: 'somewhere',
    state: 'one of them'
  }
}

const person2 = {
  name: 'James',
  age: 35,
  favoriteFood: 'watermelon',
  address: {
    city: 'somewhere else',
    state: 'another one of them'
  }
}

const person3 = {
  name: 'Bob',
  favoriteFood: 'watermelon',
}

// const {name, age} = person2
// console.log(name)
// console.log(age)

const {name: firstname, age, favoriteFood='rice'} = person2
console.log(firstname)
console.log(age)
console.log(favoriteFood)

// const{name: firstName, ...rest} = person2
// console.log(firstName)
// console.log(rest)

// const person4 = {...person1, ...person3}
// console.log(person4)

// function printUser(user)
// {
//   console.log(user)
// }

// function printUser1({name, age})
// {console.log(`The name is ${name} and age is ${age}`)
// }

// printUser1(person1)

