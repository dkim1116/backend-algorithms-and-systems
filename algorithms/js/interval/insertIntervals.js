/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    if (!intervals.length) return [newInterval];

    const result = [];
    let [newStart, newEnd] = newInterval;
    let inserted = false;

    for (let [currStart, currEnd] of intervals) {
        if (currEnd < newStart) {
            result.push([currStart, currEnd]);
        } else if (currStart > newEnd) {
            if (!inserted) {
                result.push([newStart, newEnd]);
                inserted = true;
            }
            result.push([currStart, currEnd]);
        } else {
            newStart = Math.min(currStart, newStart);
            newEnd = Math.max(currEnd, newEnd);
        }
    }

    if (!inserted) {
        result.push([newStart, newEnd]);
    }

    return result;
};