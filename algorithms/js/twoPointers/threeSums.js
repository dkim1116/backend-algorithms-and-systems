class Solution {
    threeSums(nums) {
        if (nums.length < 3) return [];

        nums.sort((a, b) => a - b);

        const result = [];

        for (let start = 0; start < nums.length - 2; start++) {
            let left = start + 1;
            let right = nums.length - 1;

            if (start > 0 && nums[start] === nums[start - 1]) continue;

            while (left < right) {
                const total = nums[start] + nums[left] + nums[right];

                if (total === 0) {
                    result.push([nums[start], nums[left], nums[right]]);
                    left++;
                    right--;

                    while (left < right && nums[right] === nums[right + 1]) right--;
                    while (left < right && nums[left] === nums[left - 1]) left++;
                } else if (total < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}