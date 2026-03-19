class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    peek() {
        return this.heap[0];
    }

    push(val, count) {
        this.heap.push([val, count]);
        this.bubbleUp();
    }

    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const top = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown();

        return top;
    }

    bubbleUp() {
        let lastIndex = this.heap.length - 1;

        while (lastIndex > 0) {
            let parentIndex = Math.floor((lastIndex - 1) / 2);

            if (this.heap[parentIndex][1] <= this.heap[lastIndex][1]) break;

            [this.heap[parentIndex], this.heap[lastIndex]] = [this.heap[lastIndex], this.heap[parentIndex]];
            lastIndex = parentIndex;
        }
    }

    bubbleDown() {
        let firstIndex = 0;
        let length = this.heap.length;

        while (true) {
            let smallestIndex = firstIndex;
            const leftIndex = firstIndex * 2 + 1;
            const rightIndex = firstIndex * 2 + 2;

            if (leftIndex < length && this.heap[leftIndex][1] < this.heap[smallestIndex][1]) smallestIndex = leftIndex;
            if (rightIndex < length && this.heap[rightIndex][1] < this.heap[smallestIndex][1]) smallestIndex = rightIndex;

            if (smallestIndex === firstIndex) break;

            [this.heap[smallestIndex], this.heap[firstIndex]] = [this.heap[firstIndex], this.heap[smallestIndex]];

            firstIndex = smallestIndex;
        }
    }
}

const topKfrequentElements = (nums, k) => {
    const freqMap = new Map();

    for (let num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }

    const minHeap = new MinHeap();

    for (let [num, count] of freqMap.entries()) {
        minHeap.push(num, count);

        if (minHeap.size() > k) minHeap.pop();
    }

    const result = [];

    while (minHeap.size()) {
        result.push(minHeap.pop()[0]);
    }

    return result;
}

//   [1,2,3,4,5]
//.     1
//.   2.    3
//. 4.  5