const mostKdistinctChar = (s, k) => {
    const countMap = new Map();

    let left = 0;
    let longest = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        countMap.set(char, (countMap.get(char) || 0) + 1);

        while (countMap.size > k) {
            const leftChar = s[left];
            countMap.set(leftChar, countMap.get(leftChar) - 1);
            left++;
        }

        longest = Math.max(longest, right - left + 1);
    }

    return longest;
}