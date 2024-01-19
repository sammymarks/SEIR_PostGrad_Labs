//BASIC RECURSION

// function sumArrayOfNums(arr, index = 0, sum = 0) {
//     if (index == arr.length) {
//         return sum
//     }
//     sum += arr[index]
//     return sumArrayOfNums(arr, index + 1, sum)
// }

// console.log(sumArrayOfNums([2, 4, 5, 8]))

//RECURSION HELPER
// function sumArrayOfNums(arr){
//     let index = 0;
//     let sum = 0;
//     // Notice the lack of parameters in rSum!
//     function rSum(){
//       if(index === arr.length){
//         return sum;
//       }
//       sum += arr[index];
//       index++;
//       return rSum();
//     }
//     // Once you’ve defined the helper function, make sure you call it!
//     return rSum();
//   }

//   console.log(sumArrayOfNums([2, 4, 5, 8]))


//PRACTICE

// Write code inside the functions
// You will have to figure out what parameters to include
// All functions must use recursion

//TESTING MOCHA


function findMax(arr, index = 0, max = arr[0]) {
    // This function returns the largest number in a given array.
    // console.log(index, arr.length, max)
    if (index == arr.length) {
        return max
    }

    if (arr[index] > max) {
        max = arr[index]
    }

    return findMax(arr, index+1, max)
}

// let one = findMax([3,4,2,1,2])
// console.log(one)
// let two =  findMax([-1, -4, -2])
// console.log(two)


// describe('findMax', ()=>{
//     it('should find the largest number in an array', ()=>{
//         let testArray = [3,4,2,1,2];
//         expect(findMax(testArray)).to.equal(4);
//     });
//     it('should work for negative numbers', ()=>{
//         let testNegatives = [-1, -4, -2];
//         expect(findMax(testNegatives)).to.equal(-1);
//     });
// })


function factorial(num, fact = num){
    // This function returns the factorial of a given number.
    num--
    if (num == 0) {return fact}
    fact = fact*num
    return factorial(num,fact)

}

// console.log(factorial(3))
// console.log(factorial(5))

// describe('factorial', ()=>{
//     it('should accurately calculate factorials', ()=>{
//         expect(factorial(3)).to.equal(6);
//         expect(factorial(5)).to.equal(120);
//     });
// })

function fibonacci(target, index = 3, min1 = 1, min2 = 1){
    // This function returns the Nth number in the fibonacci sequence.
    // https://en.wikipedia.org/wiki/Fibonacci_number
    // For this function, the first two fibonacci numbers are 1 and 1

    if (target == 0) {return 0}
    if (target == 1 || target == 2) {return 1}
    if (target == index) {return min1 + min2}
    index++
    let fib = min1 + min2
    return fibonacci(target, index, fib, min1)
}
// console.log(fibonacci(2)) //1
// console.log(fibonacci(3)) //2
// console.log(fibonacci(10)) //55


// describe('fibonacci', ()=>{
//     it('should accurately return base cases', ()=>{
//         expect(fibonacci(1)).to.equal(1);
//         expect(fibonacci(2)).to.equal(1);
//     });
//     it('should accurately calculate subsequent numbers', ()=>{
//         expect(fibonacci(3)).to.equal(2);
//         expect(fibonacci(4)).to.equal(3);
//         for(let i = 3; i < 10; i++){
//             expect(fibonacci(i)).to.equal(fibonacci(i-1)+fibonacci(i-2));
//         }
//     });
// })

function coinFlips(num, index = 1, array = ["H","T"]) {
    // This function returns an array of all possible outcomes from flipping a coin N times.
    // Input type: Integer
    // For example, coinFlips(2) would return the following:
    // ["HH", "HT", "TH", "TT"]
    // H stands for Heads and T stands for tails
    // Represent the two outcomes of each flip as "H" or "T"

    if (num == 0) {return []}
    if (num == index) {return array}
    
    index++

    let newArray = []

    array.forEach(e => newArray.push(e+"H"))
    array.forEach(e => newArray.push(e+"T"))

    return coinFlips(num, index, newArray)

}
// console.log(coinFlips(0))
// console.log(coinFlips(1))
console.log(coinFlips(2))
console.log(coinFlips(4))
console.log(coinFlips(6))



// describe('coinFlips', ()=>{
//     it('should return an array', ()=>{
//         expect(Array.isArray(coinFlips(2))).to.equal(true);
//     });
//     it("should include all possibilities", ()=>{
//         let results = coinFlips(4);
//         expect(results.includes("HHHH")).to.equal(true);
//         expect(results.includes("HTHT")).to.equal(true);
//         expect(results.includes("TTTT")).to.equal(true);
//         expect(results.length).to.equal(16);
//     });
// })


function letterCombinations(input, index = 0){
    // This function returns an array of all combinations of the given letters
    // Input type: Array of single characters
    // For example, letterCombinations(["a","b","c"]) would return the following:
    // ["a","b","c","ab","ac","ba","bc","ca","cb","abc","acb","bac","bca","cab","cba"]

    if (input.length == 0) {return []}
    


}

console.log(letterCombinations(["a","b","c"]))


// describe('letterCombinations', ()=>{
//     it("should return an array", ()=>{
//         expect(Array.isArray(letterCombinations(["a","b","c"]))).to.equal(true);
//     });
//     it("should include single letter results", ()=>{
//         expect(letterCombinations(["a","b","c"]).includes("b")).to.equal(true);
//     });
//     it("should include combinations in different order", ()=>{
//         expect(letterCombinations(["a","b","c"]).includes("ba")).to.equal(true);
//         expect(letterCombinations(["a","b","c"]).includes("ab")).to.equal(true);
//     });
//     it("should include full-length combinations", ()=>{
//         expect(letterCombinations(["a","b","c"]).includes("bac")).to.equal(true);
//         expect(letterCombinations(["a","b","c"]).includes("cab")).to.equal(true);
//     });
// })
