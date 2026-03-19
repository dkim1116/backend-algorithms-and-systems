const containMostWater = (nums) => {
    let mostWater = 0;
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const width = right - left;
        mostWater = Math.max(mostWater, width * Math.min(nums[left], nums[right]));

        if (nums[left] < nums[right]) {
            left++;
        } else {
            right--;
        }
    }

    return mostWater;
}