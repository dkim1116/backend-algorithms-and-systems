const minimumWindowSubstr = (s, t) => {
    if (t.length > s.length) return "";

    const countMap = new Map();

    for (let char of t) {
        countMap.set(char, (countMap.get(char) || 0) + 1);
    }

    let needed = t.length;
    let left = 0;

    let start = 0;
    let minLength = Infinity;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        if (countMap.has(char)) {
            if (countMap.get(char) > 0) needed--;
            countMap.set(char, countMap.get(char) - 1);
        }

        while (needed === 0) {
            if (right - left + 1 < minLength) {
                minLength = right - left + 1;
                start = left;
            }

            const leftChar = s[left];

            if (countMap.has(leftChar)) {
                if (countMap.get(leftChar) >= 0) needed++;
                countMap.set(leftChar, countMap.get(leftChar) + 1);
            }

            left++;
        }
    }

    return minLength === Infinity ? "" : s.slice(start, start + minLength);
}