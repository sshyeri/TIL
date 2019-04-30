var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)
let pick = _.sample(list)
let menu = {
    짜장면: '',
    짬뽕:'',
    볶음밥:'http://i.imgur.com/paSDPMx.jpg',
}
console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)

let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}

let getMinFromArray = nums => {
    let min = Infinity // 양의 무한대, 다른 어떤 수보다 더 큼.
    //nums 안을 돌면서...
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1, 2, 3, 4, 5, ]
console.log(getMinFromArray(ssafy))

const concat = (str1, str2) => `${str1-str2}`
const check_long_str = string => string.length > 10
