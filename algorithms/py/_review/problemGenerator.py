import random

problems = [
    "longestConsecutiveSequence.py",
    "subarraySumEqualsK.py",
    "productOfArrayItself.py",
    "combinationSum.py",
    "permutations.py",
    "subsets.py",
    "combinationSumII.py",
    "permutationsII.py",
    "binarySearch.py",
    "capacityShipPackageInNDays.py",
    "minimumDaysToMakeMBouquets.py",
    "findFirstAndLastInSortedArray.py",
    "searchRotatedSortedArray.py",
    "findMinimumInRotatedSortedArray.py",
    "splitArrayLargestSum.py",
    "findMinimumInRotatedSortedArrayII.py",
    "climbingStairs.py",
    "houseRobbersII.py",
    "minPathSumInMatrix.py",
    "houseRobbers.py",
    "minCostClimbingStairs.py",
    "courseSchedule.py",
    "numberOfIslands.py",
    "kClosestPoints.py",
    "mergeKsortedList.py",
    "topKfrequency.py",
    "insertInterval.py",
    "minMeetingRooms.py",
    "nonOverlappingIntervals.py",
    "mergeIntervals.py",
    "myCalendarII.py",
    "allAnagramsInString.py",
    "minWindowSubstr.py",
    "longestRepeatingCharRepl.py",
    "permutationInString.py",
    "longestWithoutRepeating.py",
    "mostKdistinctChar.py",
    "dailyTemperatures.py",
    "largestRectangleArea.py",
    "balancedBTree.py",
    "diameterOfBTree.py",
    "kthSmallestInBST.py",
    "binaryTreeVerticalTraversal.py",
    "isValidBST.py",
    "lca.py",
    "maxDepth.py",
    "subTreeOfAnotherTree.py",
    "levelOrderTraversal.py",
    "maxPathSum.py",
    "moveZeroes.py",
    "removeDuplicatesII.py",
    "threeSums.py",
    "trappingRainWater.py",
    "removeDuplicates.py",
    "removeElement.py",
    "threeSumsRe.py",
    "maximumProductSubarray.py",
    "maximumSubarrayWithOneDelete.py",
    "maximumSumCircularSubarray.py",
    "maximumSumSubarray.py"
]

# Shuffle once
random.shuffle(problems)

index = 0

while index < len(problems):
    input("\nPress Enter for next problem...")

    print(f"\n🔥 Problem {index + 1}: {problems[index]}")
    index += 1

print("\n✅ I've completed all problems. Restart to reshuffle.")