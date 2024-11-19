//https://www.youtube.com/watch?v=5AWRivBk0Gw&ab_channel=WebDevSimplified

class House {
	constructor(color) {
		this.color = color
	}

	getFurniture() {
		return 'sofa'
	}

}

const houseRed = new House('red')
const houseBlue = new House('blue')

console.log(houseRed.color)
console.log(houseRed.getFurniture())

console.log(houseBlue.color)
console.log(houseBlue.getFurniture())


