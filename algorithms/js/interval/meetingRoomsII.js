// const meetingRoomCount = (intervals) => {
//     const starts = intervals.map((a) => a[0]);
//     const ends = intervals.map((a) => a[1]);

//     starts.sort((a, b) => a - b);
//     ends.sort((a, b) => a - b);

//     let maxRooms = 0;
//     let left = 0;
//     let currentRooms = 0;

//     for (let right = 0; right < starts.length; right++) {
//         if (starts[right] >= ends[left]) {
//             currentRooms--;
//             left++;
//         }

//         currentRooms++;
//         maxRooms = Math.max(maxRooms, currentRooms);
//     }

//     return minimumRoom;
// }

const meetingRoomCount = (intervals) => {
    const starts = intervals.map((a) => a[0]);
    const ends = intervals.map((a) => a[1]);

    starts.sort((a, b) => a - b);
    ends.sort((a, b) => a - b);

    let startPointer = 0;
    let endPointer = 0;
    let currentRoomCount = 0;
    let maxRoomCount = 0;

    while (startPointer < starts.length) {
        if (starts[startPointer] >= ends[endPointer]) {
            currentRoomCount--;
            endPointer++;
        }

        currentRoomCount++;
        maxRoomCount = Math.max(maxRoomCount, currentRoomCount);

        startPointer++;
    }

    return maxRoomCount;
}

