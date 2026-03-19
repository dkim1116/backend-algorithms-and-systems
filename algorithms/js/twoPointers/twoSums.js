// Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

// You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

// Return the answer with the smaller index first.

const twoSumWithPointers = (nums, target) => {
    const numTuples = nums.map((n, i) => [n, i]);
    
    numTuples.sort((a, b) => a[0] - b[0]);

    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let sum = numTuples[left][0] + numTuples[right][0];

        if (sum === target) {
            return [numTuples[left][1], numTuples[right][1]];
        }

        if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return [];
}