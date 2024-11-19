//compiling and variables
var bob = "hey I'm bob";
var bob2 = function () { };
console.log(bob);
var a = 5.321;
var obj = {
    x: 3.45,
    y: 7
};
var obj2 = { x: 23, y: 30 };
obj2.z = 5;
//functions
var add = function (x, y) {
    x + y;
};
var add2 = function (x, y) { return x + y; };
//add2(123, obj2);
var add3 = function (_a) {
    var a = _a.a, b = _a.b;
    a + b;
};
//unions
var maybeNum = 5;
maybeNum = "hello";
var dogCat = {
    bark: "bark",
    purr: "purr"
};
//casting
add(dogCat, dogCat);
//any
var doesAnything = function (x) {
    console.log(x);
};
doesAnything(function () { return 5; });
