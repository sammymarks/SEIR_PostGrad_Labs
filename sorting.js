// Sorting Questions - https://www.techiedelight.com/sorting-interview-questions/


//bubble sort

const bubbleSort = (size) => {

    let rand = []
    for (let i=0; i<size; i++) {
        rand.push(Math.floor(Math.random()*100))
    }

    console.log("rand", rand)


    //

    let repeat = true


    while (repeat == true) {
        let flipCount = 0

        for (let i=0; i<(rand.length-1); i++) {

            let one = rand[i]
            let two = rand[i+1]


            if (one > two) {
                rand[i] = two
                rand[i+1] = one
                flipCount++
            }

        }
        if (flipCount == 0) {repeat = false}
    }
    return rand
}

// console.log(bubbleSort(10))

//insertion sort

const insertionSort = (size) => {
    
    //create a random array
    let rand = []
    for (let i=0; i<size; i++) {
        rand.push(Math.floor(Math.random()*100))
    }

    console.log("rand", rand)

    //create the output array starting with the first element in rand
    //for each element in rand, find the right place in output and remove from rand
    let output = [rand[0]]
    
    for (let j=1; j<rand.length; j++) {
        // console.log ("current output", output)
        // console.log(j, rand[j])
        //check special cases (largest and smallest)
        //check each pair and insert at location
        //special case - rand[0] is the smallest
        if (rand[j]<output[0]) {
            console.log("SMALLEST")
            output.unshift(rand[j])
        //special case - rand[0] is the largest
        } else if (rand[j]>output[output.length - 1]) {
            console.log("LARGEST")
            output.push(rand[j])
        } else {
            console.log("MIDDLE")
            console.log(rand[j])
            let index

            for (let k = 0; k<output.length; k++ ) {
                if (rand[j]>output[k] && rand[j]<output[k+1]) {
                    console.log("found index")
                    console.log("k", k)
                    console.log("left", output[k])
                    console.log("right", output[k+1])
                
                    index = k
                }
            }
            console.log(index)
            output.splice(index+1,0,rand[j])

        }
        
        console.log("ending output", output)
    }

    return(output)
}

// console.log(insertionSort(5))




//BUCKET SORT

//figure out the highest number
//figure out the lowest number
//figure out the number of buckets based on sqrt arr.length
//define boundaries for buckets
//place each item into its respective bucket
//sort each bucket
//join the sorted buckets together


const bucketSort = (arr) => {
    console.log(arr)
    let numBuckets = Math.floor(Math.sqrt(arr.length))
    return numBuckets

}



console.log(bucketSort([12,6,3,7,13,8]))
console.log(bucketSort([-3, -1, 5, 100]))
console.log(bucketSort([-3, -1, 5, 100]))
