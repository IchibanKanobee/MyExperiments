// https://www.youtube.com/watch?v=DHvZLI7Db8E&ab_channel=WebDevSimplified

let p = new Promise((resolve, reject) => {
    let a = 1 + 2
    if (a == 2) {
        resolve ('Success')
    }
    else if (a == 3) {
        reject('Failed')
    }
})

p.then((message) => { 
    console.log('This is in then ' + message)
}).catch((message) => {
    console.log('This is the the catch ' + message)
})

