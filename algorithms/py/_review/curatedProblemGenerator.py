import random

problems = [
    # Binary Search
    # {"name": "Binary Search", "link": "https://leetcode.com/problems/binary-search/"},
    {"name": "Search in Rotated Sorted Array", "link": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
    # {"name": "Find First and Last Position of Element in Sorted Array", "link": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"},
    {"name": "Split Array Largest Sum", "link": "https://leetcode.com/problems/split-array-largest-sum/"},
    # {"name": "Capacity To Ship Packages Within D Days", "link": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/"},
    {"name": "Minimum Number of Days to Make m Bouquets", "link": "https://leetcode.com/problems/minimum-number-of-days-to-make-bouquets/"},
    {"name": "Magnetic Force Between Two Balls", "link": "https://leetcode.com/problems/magnetic-force-between-two-balls/"},
    # Sliding Window
    {"name": "Minimum Window Substring", "link": "https://leetcode.com/problems/minimum-window-substring/"},
    {"name": "Longest Repeating Character Replacement", "link": "https://leetcode.com/problems/longest-repeating-character-replacement/"},
    {"name": "Permutation in String", "link": "https://leetcode.com/problems/permutation-in-string/"},
    # Arrays
    {"name": "Subarray Sum Equals K", "link": "https://leetcode.com/problems/subarray-sum-equals-k/"},
    {"name": "Longest Consecutive Sequence", "link": "https://leetcode.com/problems/longest-consecutive-sequence/"},
    # {"name": "Product of Array Except Self", "link": "https://leetcode.com/problems/product-of-array-except-self/"},
    # Backtracking
    # {"name": "Subsets", "link": "https://leetcode.com/problems/subsets/"},
    {"name": "Combination Sum", "link": "https://leetcode.com/problems/combination-sum/"},
    {"name": "Combination Sum II", "link": "https://leetcode.com/problems/combination-sum-ii/"},
    {"name": "Permutations", "link": "https://leetcode.com/problems/permutations/"},
    # Trees
    {"name": "Binary Tree Maximum Path Sum", "link": "https://leetcode.com/problems/binary-tree-maximum-path-sum/"},
    {"name": "Diameter of Binary Tree", "link": "https://leetcode.com/problems/diameter-of-binary-tree/"},
    {"name": "Lowest Common Ancestor of a Binary Tree", "link": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/"},
    {"name": "Validate Binary Search Tree", "link": "https://leetcode.com/problems/validate-binary-search-tree/"},
    {"name": "Kth Smallest Element in a BST", "link": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/"},
    # {"name": "Binary Tree Level Order Traversal", "link": "https://leetcode.com/problems/binary-tree-level-order-traversal/"},
    # Graphs
    {"name": "Course Schedule", "link": "https://leetcode.com/problems/course-schedule/"},
    {"name": "Number of Islands", "link": "https://leetcode.com/problems/number-of-islands/"},
    {"name": "Clone Graph", "link": "https://leetcode.com/problems/clone-graph/"},
    # Heaps
    {"name": "K Closest Points to Origin", "link": "https://leetcode.com/problems/k-closest-points-to-origin/"},
    {"name": "Top K Frequent Elements", "link": "https://leetcode.com/problems/top-k-frequent-elements/"},
    {"name": "Merge k Sorted Lists", "link": "https://leetcode.com/problems/merge-k-sorted-lists/"},
    # Intervals
    {"name": "Insert Interval", "link": "https://leetcode.com/problems/insert-interval/"},
    {"name": "Merge Intervals", "link": "https://leetcode.com/problems/merge-intervals/"},
    {"name": "Non-overlapping Intervals", "link": "https://leetcode.com/problems/non-overlapping-intervals/"},
    # {"name": "Meeting Rooms II", "link": "https://leetcode.com/problems/meeting-rooms-ii/"},
    # {"name": "My Calendar II", "link": "https://leetcode.com/problems/my-calendar-ii/"},
    # Monotonic Stack
    {"name": "Daily Temperatures", "link": "https://leetcode.com/problems/daily-temperatures/"},
    {"name": "Largest Rectangle in Histogram", "link": "https://leetcode.com/problems/largest-rectangle-in-histogram/"},
    
    {"name": "3Sum", "link": "https://leetcode.com/problems/3sum/"},
    {"name": "Trapping Rain Water", "link": "https://leetcode.com/problems/trapping-rain-water/"},
    {"name": "Move Zeroes", "link": "https://leetcode.com/problems/move-zeroes/"},
    # DP
    {"name": "House Robber", "link": "https://leetcode.com/problems/house-robber/"},
    {"name": "Minimum Path Sum", "link": "https://leetcode.com/problems/minimum-path-sum/"},
    {"name": "Maximum Product Subarray", "link": "https://leetcode.com/problems/maximum-product-subarray/"},
    {"name": "Maximum Subarray", "link": "https://leetcode.com/problems/maximum-subarray/"},
    {"name": "Maximum Sum Circular Subarray", "link": "https://leetcode.com/problems/maximum-sum-circular-subarray/"},
    {"name": "Maximum Subarray Sum With One Deletion", "link": "https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/"},
    {"name": "Longest Increasing Subsequence", "link": "https://leetcode.com/problems/longest-increasing-subsequence/"},
    {"name": "Coin Change", "link": "https://leetcode.com/problems/coin-change/"},
    
    # Not yet {"name": "Single Number", "link": "https://leetcode.com/problems/single-number/"},
    # Trie
    {"name": "Word Search II", "link": "https://leetcode.com/problems/word-search-ii"},
]

# Shuffle once
random.shuffle(problems)

index = 0

while index < len(problems):
    input("\nPress Enter for next problem...")
    problem = problems[index]
    print(f"\n🔥 Problem {index + 1}: {problem['name']}")
    print(f"🔗 {problem['link']}")
    index += 1

print("\n✅ I've completed all problems. Restart to reshuffle.")