const trapRainWater = (nums) => {
    let left = 0;
    let right = nums.length - 1;
    let leftMax = 0;
    let rightMax = 0;
    let rainCount = 0;

    while (left < right) {
        if (nums[left] < nums[right]) {
            if (nums[left] >= leftMax) {
                leftMax = nums[left];
            } else {
                rainCount += leftMax - nums[left];
            }
            left++;
        } else {
            if (nums[right] >= rightMax) {
                rightMax = nums[right];
            } else {
                rainCount += rightMax - nums[right];
            }
            right--;
        }
    }

    return rainCount;
}