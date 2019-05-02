// let 블록 스코프 예제
{
    let x = '강혜리'
    console.log(x) // 강혜리
    {
        let x = 1
        console.log(x) // 1
    }
    console.log(x) // 강혜리
}
console.log(typeof x) //undefined

let foo
let bar = undefined

foo // undefined
bar // undefined

baz // ReferenceError baz is not defined

// 우리가 쓴 코드
y
var y = 1
y

// JS가 이해한 코드
var y
y   // undefined
y = 1 // 1
y   // 1


if(x !== 1) {
    console.log(y) //undefined
    var y = 3
    if (y === 3) {
        var x = 1
    }
    console.log(y)  // 3
}
if(x === 1) {
    console.log(y)  // 3
}


//var 로 변수를 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다.
var x = 1
if (x === 1) {
    var x = 2
    console.log(x) // 2
}
console.log(x) // 2
// JS가 이해한 코드
var x 
x = 1
if(x === 1){
    x = 2
    console.log(x)
}
console.log(x)

//함수도 호이스팅이 가능
//ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태
ssafy()
function ssafy() { 
    console.log('hoisting!!')
}

// 변수에 할당한 함수는 호이스팅 되지 않는다.
let ssafy = function() {
    console.log('hoisting!!')
}