// Given an array of integers nums and an integer k, 
// return the total number of subarrays whose sum equals to k.

// A subarray is a contiguous non-empty sequence of elements within an array.

// Pattern: Subarray sum → Prefix Sum + HashMap

// Invariant:
// The hashmap stores how many times each prefix sum has appeared so far.

// Action:
// As we iterate through the array we maintain a runningSum.
// If runningSum - k has appeared before, then a subarray ending here sums to k.
// We add the frequency of (runningSum - k) to the count.
// Then we record the current runningSum in the hashmap.

// Why:
// prefixSum[i] - prefixSum[j] = k
// Therefore prefixSum[j] = prefixSum[i] - k
// If we've seen prefixSum[i] - k before, that means a valid subarray exists.

const subarraySum = (nums, k) => {
    let count = 0;
    let runningSum = 0;
    const sumMap = new Map();
    sumMap.set(runningSum, 1);

    for (let num of nums) {
        // CurrentTotalSum - previousRunningSum = k
        // -previousRunningSum = k - CurrentTotalSum
        // previousRunningSum = -k + CurrentTotalSum

        runningSum += num;
        if (sumMap.has(runningSum - k)) {
            count += sumMap.get(runningSum - k);
        }

        sumMap.set(runningSum, (sumMap.get(runningSum) || 0) + 1);
    }

    return count;
}