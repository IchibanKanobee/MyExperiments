//https://www.youtube.com/watch?v=R8rmfD9Y5-c&ab_channel=WebDevSimplified
const items = [
    {name: 'Bike',  price: 100},
    {name: 'TV',  price: 200},
    {name: 'Album',  price: 10},
    {name: 'Book',  price: 5},
    {name: 'Phone',  price: 500},
    {name: 'Computer',  price: 1000},
    {name: 'Keyboard',  price: 25},
];

//filter
const filteredItems = items.filter((item) => {
    return item.price <= 100;
});

console.log(filteredItems)

//map
const mappedItems = items.map((item) => {
    return item.name;
});

console.log(mappedItems)

//find (returns first item that is true)
const foundItem = items.find((item) => {
    return item.name === 'Book';
});
console.log(foundItem)


//for each
items.forEach((item) => {
console.log(item.name)
})

//some
const hasInexpensiveItems = items.some((item) => {
    return item.price < 50;
})
console.log(hasInexpensiveItems)

//every
const allExpensiveItems = items.every((item) => {
    return item.price > 1000;
})
console.log(allExpensiveItems)

//reduce
const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal;
}, 0)

console.log(total)

//includes
const arr = [1,2,3,4,5]
const includesTwo = arr.includes(2)

console.log(includesTwo)