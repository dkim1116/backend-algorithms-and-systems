const topKfrequentElements = (nums, k) => {
    const frequencyMap = new Map();

    for (let num of nums) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    }

    const frequencyBucket = new Array(nums.length + 1).fill(0).map(() => []);

    for (let [num, count] of frequencyMap.entries()) {
        frequencyBucket[count].push(num);
    }

    const result = [];

    for (let i = frequencyBucket.length - 1; i >= 0; i--) {
        for (let num of frequencyBucket[i]) {
            result.push(num);
        }
    }

    return result.slice(0, k);
}