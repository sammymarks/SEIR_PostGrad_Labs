// Sorting Questions - https://www.techiedelight.com/sorting-interview-questions/

const randomArray = (size) => {
    let rand = []
    for (let i=0; i<size; i++) {
        rand.push(Math.floor(Math.random()*100))
    }
    return rand
}


//bubble sort

const bubbleSort = (arr) => {
    // console.log("BUBBLE SORT")
    // console.log(arr)

    //

    let repeat = true


    while (repeat == true) {
        let flipCount = 0

        for (let i=0; i<(arr.length-1); i++) {

            let one = arr[i]
            let two = arr[i+1]


            if (one > two) {
                arr[i] = two
                arr[i+1] = one
                flipCount++
            }

        }
        if (flipCount == 0) {repeat = false}
    }
    return arr
}

// console.log(bubbleSort(randomArray(10)))

//insertion sort

const insertionSort = (arr) => {
    console.log("INSERTION SORT")
    console.log(arr)
    //create a random array

    //create the output array starting with the first element in rand
    //for each element in rand, find the right place in output and remove from rand
    let output = [arr[0]]
    
    for (let j=1; j<arr.length; j++) {
        // console.log ("current output", output)
        // console.log(j, arr[j])
        //check special cases (largest and smallest)
        //check each pair and insert at location
        //special case - arr[0] is the smallest
        if (arr[j]<output[0]) {
            console.log("SMALLEST")
            output.unshift(arr[j])
        //special case - arr[0] is the largest
        } else if (arr[j]>output[output.length - 1]) {
            console.log("LARGEST")
            output.push(arr[j])
        } else {
            console.log("MIDDLE")
            console.log(arr[j])
            let index

            for (let k = 0; k<output.length; k++ ) {
                if (arr[j]>output[k] && arr[j]<output[k+1]) {
                    console.log("found index")
                    console.log("k", k)
                    console.log("left", output[k])
                    console.log("right", output[k+1])
                
                    index = k
                }
            }
            console.log(index)
            output.splice(index+1,0,arr[j])

        }
        
        console.log("ending output", output)
    }

    return(output)
}

// console.log(insertionSort(randomArray(10)))

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
    
    //get array characteristics
    let numBuckets = Math.floor(Math.sqrt(arr.length))
    let top = Math.max(...arr)
    let bottom = Math.min(...arr)
    // console.log(min, max)
    let range = top-bottom
    let bucketSize = range/numBuckets
    
    //create placeholder buckets and bucket ranges
    let bucketRanges = {}
    let buckets = []


    //define bucket ranges with the key being the value of the bucket index
    for (let i=0; i<numBuckets; i++) {
        bucketRanges[i]={}
        buckets[i] = [] 
        if (i==0) {
            bucketRanges[i].min = bottom
            bucketRanges[i].max = bottom+bucketSize
        } else if (i==(numBuckets-1)){
            bucketRanges[i].min = bucketRanges[i-1].max
            bucketRanges[i].max = top
        } else {
            bucketRanges[i].min = bucketRanges[i-1].max
            bucketRanges[i].max = bucketRanges[i].min + bucketSize
        }
    }

    console.log("bucketRanges", bucketRanges)

    //for each array number, loop through the bucket ranges to check the right bucket and push the number in the right bucket
    for (let j=0; j<arr.length; j++) {
        //special case
        if (arr[j]==bottom) {
            buckets[0].push(arr[j])
        } else {
            for (let k=0; k<numBuckets; k++) {
                if (arr[j]>bucketRanges[k].min && arr[j]<=bucketRanges[k].max) {
                    buckets[k].push(arr[j])
                }
            }
        }
    }

    //sort and concatanate each bucket
    buckets.forEach(a=>bubbleSort(a))
    let output = [].concat(...buckets)
    return output
}



console.log(bucketSort([12, 6, 3, 7, 13, 8]))
console.log(bucketSort([-3, -1, 5, 100]))
console.log(bucketSort([-3, -1, 5, 101, 115, 78, 51, 52, 100]))

