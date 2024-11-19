//compiling and variables
const bob = "hey I'm bob";
const bob2 = () => {};
console.log(bob);

const a = 5.321;
const obj = {
  x: 3.45,
  y: 7,
};

interface MyObj {
  x: number;
  y: number;
  z?: number;
}

const obj2: MyObj = { x: 23, y: 30 };

obj2.z = 5;
//functions

const add = (x: number, y: number) => {
  x + y;
};

type AddFunc = (x: number, y: number) => number;

const add2: AddFunc = (x: number, y: number) => x + y;

//add2(123, obj2);

const add3 = ({ a, b }: { a: number; b: number }) => {
  a + b;
};

//unions
let maybeNum: number | string = 5;
maybeNum = "hello"

interface Dog {
    bark: string
}

interface Cat {
    purr: string
}

type DogCat = Dog & Cat | number | string;

let dogCat: DogCat = { 
    bark: "bark",
    purr: "purr"
}

//casting

add(dogCat as number, dogCat as number )
//any
const doesAnything = (x:any) => {
    console.log(x)
};

doesAnything(() => 5)