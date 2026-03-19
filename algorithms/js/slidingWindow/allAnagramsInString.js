const findAllAnagramsInString = (s, t) => {
    if (t.length > s.length) return [];

    const result = [];

    const countMap = new Map();

    for (let char of t) {
        countMap.set(char, (countMap.get(char) || 0) + 1);
    }

    let needed = t.length;
    let left = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        if (countMap.has(char)) {
            if (countMap.get(char) > 0) needed--;
            countMap.set(char, countMap.get(char) - 1);
        }

        if (right - left + 1 > t.length) {
            const leftChar = t[left];

            if (countMap.has(leftChar)) {
                if (countMap.get(leftChar) >= 0) needed++;

                countMap.set(leftChar, countMap.get(leftChar)++);
            }

            left++
        }

        if (needed === 0) result.push(left)
    }

    return result;
}