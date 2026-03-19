/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    const result = [];

    for (let [currStart, currEnd] of intervals) {
        if (!result.length) {
            result.push([currStart, currEnd]);
            continue;
        }

        const [prevStart, prevEnd] = result[result.length - 1];

        if (currStart <= prevEnd) {
            result[result.length - 1] = [prevStart, Math.max(currEnd, prevEnd)];
        } else {
            result.push([currStart, currEnd]);
        }
    }

    return result;
};