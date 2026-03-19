// Restate: Find the minimum number of arrows 
// needed to burst all balloons represented by intervals.
// Pattern: Sort by end points and shoot arros at earliest end points
// Invariant: We keep track of the end of the last burst balloon interval at all times
// Action: Sort the intervals in ascending order by their end times. 
// Earliest endpoint becomes the first arrow position. Save the end time and skip through 
// all intervals that start before or at this end time. When we find an interval that doesnt overlap,
// we need another arrow, so we increment the arrow count and update the end time to this new interval's end time.
// Why: This works because by always shooting at the earliest end time, we maximize the number of balloons burst with each arrow.

const burstBalloons = (points) => {
    if (points.length === 0) return 0;

    points.sort((a, b) => a[1] - b[1]);

    let arrowPos;
    let arrowCount = 0;

    for (let [start, end] of points) {
        if (arrowPos === undefined) {
            arrowPos = end;
            arrowCount++;
            continue;
        }

        if (start <= arrowPos && arrowPos <= end) {
            continue;
        } else {
            arrowPos = end;
            arrowCount++;
        }
    
    }

    return arrowCount;
}