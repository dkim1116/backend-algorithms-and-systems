const scheduling = (intervals) => {
    intervals.sort((a, b) => a[1] - b[1]);

    let count = 0;
    let lastEnd;

    for (let [start, end] of intervals) {
        if (lastEnd === undefined) {
            lastEnd = end;
            count++;
            continue;
        }

        if (start > lastEnd) {
            lastEnd = end;
            count++;
        }
    }

    return count;
}