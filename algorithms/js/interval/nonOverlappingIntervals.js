/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    const result = [];
    let removalCount = 0;
    let prevEnd;

    for (let [currStart, currEnd] of intervals) {
        if (prevEnd === undefined) {
            prevEnd = currEnd;
            continue;
        }

        if (prevEnd > currStart) {
            prevEnd = Math.min(prevEnd, currEnd);
            removalCount++;
        } else {
            prevEnd = currEnd;
        }
    }

    return removalCount;
};