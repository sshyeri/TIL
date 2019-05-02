const nothing = () => { console.log('complete')}

console.log('start sleeping')
// non_block callback stack에서 3초 실행중 : 동시에 실행되는 것처럼 보임
setTimeout(nothing, 3000) 
console.log('end of program')

//python code 처럼 동작하게 하려면
const logEnd = () => {
    console.log('end of program')
}
console.log('start sleeping')
setTimeout(logEnd, 3000)

function first() {
    console.log('first')
}
function second() {
    console.log('second')
}
function third() {
console.log('third')
}
first()
setTimeout(second, 0)
third()


function func3() {
    console.log('func3')
}
function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}
function func1() {
    console.log('func1')
    func2()   
}
func1()
