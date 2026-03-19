const permInString = (s1, s2) => {
    if (s1.length > s2.length) return false;

    const countMap = new Map();

    for (let char of s1) {
        countMap.set(char, (countMap.get(char) || 0) + 1);
    }

    let needed = s1.length;
    let left = 0;

    for (let right = 0; right < s2.length; right++) {
        const char = s2[right];

        if (countMap.has(char)) {
            if (countMap.get(char) > 0) needed--;
            countMap.set(char, countMap.get(char) - 1);
        }

        if (right - left + 1 > s1.length) {
            const leftChar = s2[left];
            if (countMap.has(leftChar)) {
                if (countMap.get(leftChar) >= 0) needed++;
                countMap.set(leftChar, countMap.get(leftChar) + 1);
            }

            left++;
        }

        if (needed === 0) return true;
    }

    return false;
}