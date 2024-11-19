const items = [
    {name: "Bike", price: 100},
    {name: "TV", price: 200},
    {name: "Album", price: 10},
    {name: "Book", price: 5},
    {name: "Phone", price: 500},
    {name: "Computer", price: 1000},
    {name: "Keyboard", price: 25}
];

const filteredItems = items.filter((item) => {
    return item.price <=100
})

const itemNames = items.map((item) => {
    return item.name
})

const foundNames = items.find((item) => {
    return item.name === "Book"
})

items.forEach((item) => {
    console.log (item.name)
})

const hasInexpensiveItems = items.some((item) => {
    return item.price <= 100
})

const allInexpensiveItems = items.every((item) => {
    return item.price <= 100
})


const total = items.reduce((currenTotal, item) => {
    return item.price + currenTotal
}, 0)


console.log(items)
console.log(filteredItems)
console.log(itemNames)
console.log(foundNames)
console.log(hasInexpensiveItems)
console.log(allInexpensiveItems)
console.log(total)

const includedItems = [1,2,3,4,5]

const includesTwo = includedItems.includes(2)
console.log(includesTwo)
