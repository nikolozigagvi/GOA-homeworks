let nums = [1 , 2, 3, 4, 5, 6, 7, 8, 98]

console.log(nums.some(num => num%2 === 0))
console.log(nums.every(num => num%2 === 0))



let listi = [1 , 3, 4, 5,7, 9,67 ]

let litimteliori = listi.map((num , index ) => {
    return `${num}: ${index}`
})

console.log(litimteliori)



let arrrrr = [67 , 41 ,21 , 42 , 61 , 100 , 50 , 60 , 7]

let newarr = arrrrr.filter(num => num%5 === 0)

console.log(newarr)