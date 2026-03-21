# Bucket Sort
class SolutionBucket:
    def topKfrequency(self, nums: list[int], k: int) -> list[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        freqBucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqBucket[freq].append(num)

        result = []

        for i in reversed(range(len(freqBucket))):
            for num in freqBucket[i]:
                result.append(num)

        return result[:k]
    
import heapq
# Heap
class SolutionHeap:
    def topKfrequency(self, nums: list[int], k: int) -> list[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        minHeap = []

        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for freq, num in minHeap]
        