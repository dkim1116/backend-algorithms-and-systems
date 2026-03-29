from __future__ import annotations

from pathlib import Path
from textwrap import dedent


REVIEW_DIR = Path(__file__).resolve().parent / "review"

TREE_NODE = """
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
"""

LIST_NODE = """
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next
"""

GRAPH_NODE = """
class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

SPECS = [
    {
        "filename": "case01_shifted_lookup.py",
        "title": "Shifted Lookup",
        "prompt": [
            "A strictly increasing array was rotated once at an unknown pivot.",
            "Given the rotated array and a target value, return the target index or -1 if it is missing.",
            "Aim for logarithmic time.",
        ],
        "examples": [
            "Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0",
            "Output: 4",
            "Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3",
            "Output: -1",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        pass
""",
    },
    {
        "filename": "case02_load_balancer.py",
        "title": "Load Balancer",
        "prompt": [
            "You must split an array into exactly k non-empty contiguous groups.",
            "The score of a split is the largest group sum.",
            "Return the smallest possible score across all valid splits.",
        ],
        "examples": [
            "Input: nums = [7, 2, 5, 10, 8], k = 2",
            "Output: 18",
            "Input: nums = [1, 2, 3, 4, 5], k = 2",
            "Output: 9",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        pass
""",
    },
    {
        "filename": "case03_bloom_deadline.py",
        "title": "Bloom Deadline",
        "prompt": [
            "flowers[i] is the day the i-th flower opens.",
            "Build m bouquets using exactly k adjacent open flowers per bouquet.",
            "Return the minimum day when this becomes possible, or -1 if it never can.",
        ],
        "examples": [
            "Input: flowers = [1, 10, 3, 10, 2], m = 3, k = 1",
            "Output: 3",
            "Input: flowers = [1, 10, 3, 10, 2], m = 3, k = 2",
            "Output: -1",
        ],
        "starter": """
class Solution:
    def solve(self, flowers: list[int], m: int, k: int) -> int:
        pass
""",
    },
    {
        "filename": "case04_max_gap_placement.py",
        "title": "Max Gap Placement",
        "prompt": [
            "You are given basket positions on a number line.",
            "Place m balls so that the minimum distance between any two placed balls is as large as possible.",
            "Return that best possible minimum distance.",
        ],
        "examples": [
            "Input: positions = [1, 2, 3, 4, 7], m = 3",
            "Output: 3",
            "Input: positions = [5, 4, 3, 2, 1, 1000000000], m = 2",
            "Output: 999999999",
        ],
        "starter": """
class Solution:
    def solve(self, positions: list[int], m: int) -> int:
        pass
""",
    },
    {
        "filename": "case05_tight_cover.py",
        "title": "Tight Cover",
        "prompt": [
            "Given strings source and need, find the shortest substring of source that contains every character from need with the required counts.",
            "Return an empty string if no such substring exists.",
        ],
        "examples": [
            "Input: source = 'ADOBECODEBANC', need = 'ABC'",
            "Output: 'BANC'",
            "Input: source = 'a', need = 'aa'",
            "Output: ''",
        ],
        "starter": """
class Solution:
    def solve(self, source: str, need: str) -> str:
        pass
""",
    },
    {
        "filename": "case06_uniform_stretch.py",
        "title": "Uniform Stretch",
        "prompt": [
            "You may replace at most k characters in a string.",
            "Return the length of the longest substring that can be turned into one repeated letter after those replacements.",
        ],
        "examples": [
            "Input: s = 'ABAB', k = 2",
            "Output: 4",
            "Input: s = 'AABABBA', k = 1",
            "Output: 4",
        ],
        "starter": """
class Solution:
    def solve(self, s: str, k: int) -> int:
        pass
""",
    },
    {
        "filename": "case07_hidden_anagram.py",
        "title": "Hidden Anagram",
        "prompt": [
            "Return True if any substring of s2 is a permutation of s1.",
            "Otherwise return False.",
        ],
        "examples": [
            "Input: s1 = 'ab', s2 = 'eidbaooo'",
            "Output: True",
            "Input: s1 = 'ab', s2 = 'eidboaoo'",
            "Output: False",
        ],
        "starter": """
class Solution:
    def solve(self, s1: str, s2: str) -> bool:
        pass
""",
    },
    {
        "filename": "case08_target_runs.py",
        "title": "Target Runs",
        "prompt": [
            "Count how many contiguous subarrays sum to k.",
            "The array may contain positive, zero, and negative values.",
        ],
        "examples": [
            "Input: nums = [1, 1, 1], k = 2",
            "Output: 2",
            "Input: nums = [1, 2, 3], k = 3",
            "Output: 2",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        pass
""",
    },
    {
        "filename": "case09_streak_length.py",
        "title": "Streak Length",
        "prompt": [
            "Given an unsorted list of integers, return the length of the longest run of consecutive values.",
            "Your solution should be near linear time.",
        ],
        "examples": [
            "Input: nums = [100, 4, 200, 1, 3, 2]",
            "Output: 4",
            "Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]",
            "Output: 9",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case10_unlimited_recipe.py",
        "title": "Unlimited Recipe",
        "prompt": [
            "You are given distinct ingredient values and a target total.",
            "Return all unique combinations that sum to the target.",
            "You may reuse each ingredient any number of times.",
        ],
        "examples": [
            "Input: values = [2, 3, 6, 7], target = 7",
            "Output: [[2, 2, 3], [7]]",
            "Input: values = [2, 3, 5], target = 8",
            "Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]",
        ],
        "starter": """
class Solution:
    def solve(self, values: list[int], target: int) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case11_single_use_recipe.py",
        "title": "Single Use Recipe",
        "prompt": [
            "You are given ingredient values that may contain duplicates and a target total.",
            "Return all unique combinations that sum to target.",
            "Each array element may be used at most once.",
        ],
        "examples": [
            "Input: values = [10, 1, 2, 7, 6, 1, 5], target = 8",
            "Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]",
            "Input: values = [2, 5, 2, 1, 2], target = 5",
            "Output: [[1, 2, 2], [5]]",
        ],
        "starter": """
class Solution:
    def solve(self, values: list[int], target: int) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case12_full_arrangements.py",
        "title": "Full Arrangements",
        "prompt": [
            "Return every possible ordering of the given distinct integers.",
        ],
        "examples": [
            "Input: nums = [1, 2, 3]",
            "Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]",
            "Input: nums = [0, 1]",
            "Output: [[0, 1], [1, 0]]",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case13_best_branch_route.py",
        "title": "Best Branch Route",
        "support": TREE_NODE,
        "prompt": [
            "A path in a binary tree may start and end at any nodes, but it must move through parent-child connections.",
            "Return the maximum possible path sum.",
        ],
        "examples": [
            "Input: root = [1, 2, 3]",
            "Output: 6",
            "Input: root = [-10, 9, 20, null, null, 15, 7]",
            "Output: 42",
        ],
        "starter": """
class Solution:
    def solve(self, root: TreeNode | None) -> int:
        pass
""",
    },
    {
        "filename": "case14_tree_span.py",
        "title": "Tree Span",
        "support": TREE_NODE,
        "prompt": [
            "The span of a binary tree is the number of edges in the longest path between any two nodes.",
            "Return that value.",
        ],
        "examples": [
            "Input: root = [1, 2, 3, 4, 5]",
            "Output: 3",
            "Input: root = [1, 2]",
            "Output: 1",
        ],
        "starter": """
class Solution:
    def solve(self, root: TreeNode | None) -> int:
        pass
""",
    },
    {
        "filename": "case15_shared_ancestor.py",
        "title": "Shared Ancestor",
        "support": TREE_NODE,
        "prompt": [
            "Given the root of a binary tree and two nodes p and q that both exist in the tree, return their lowest common ancestor.",
        ],
        "examples": [
            "Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1",
            "Output: 3",
            "Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4",
            "Output: 5",
        ],
        "starter": """
class Solution:
    def solve(
        self,
        root: TreeNode | None,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode | None:
        pass
""",
    },
    {
        "filename": "case16_ordered_tree_check.py",
        "title": "Ordered Tree Check",
        "support": TREE_NODE,
        "prompt": [
            "Return True if the binary tree satisfies strict binary search tree ordering rules at every node.",
            "Otherwise return False.",
        ],
        "examples": [
            "Input: root = [2, 1, 3]",
            "Output: True",
            "Input: root = [5, 1, 4, null, null, 3, 6]",
            "Output: False",
        ],
        "starter": """
class Solution:
    def solve(self, root: TreeNode | None) -> bool:
        pass
""",
    },
    {
        "filename": "case17_rank_in_ordered_tree.py",
        "title": "Rank In Ordered Tree",
        "support": TREE_NODE,
        "prompt": [
            "Given a binary search tree, return the k-th smallest value in sorted order.",
        ],
        "examples": [
            "Input: root = [3, 1, 4, null, 2], k = 1",
            "Output: 1",
            "Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3",
            "Output: 3",
        ],
        "starter": """
class Solution:
    def solve(self, root: TreeNode | None, k: int) -> int:
        pass
""",
    },
    {
        "filename": "case18_dependency_finish.py",
        "title": "Dependency Finish",
        "prompt": [
            "There are numCourses labeled from 0 to numCourses - 1.",
            "Each pair [a, b] means b must be completed before a.",
            "Return True if it is possible to finish all courses.",
        ],
        "examples": [
            "Input: numCourses = 2, prerequisites = [[1, 0]]",
            "Output: True",
            "Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]",
            "Output: False",
        ],
        "starter": """
class Solution:
    def solve(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pass
""",
    },
    {
        "filename": "case19_land_clusters.py",
        "title": "Land Clusters",
        "prompt": [
            "A grid contains '1' for land and '0' for water.",
            "Count how many disconnected land masses exist using 4-directional adjacency.",
        ],
        "examples": [
            "Input: grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]",
            "Output: 1",
            "Input: grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]",
            "Output: 3",
        ],
        "starter": """
class Solution:
    def solve(self, grid: list[list[str]]) -> int:
        pass
""",
    },
    {
        "filename": "case20_graph_copy.py",
        "title": "Graph Copy",
        "support": GRAPH_NODE,
        "prompt": [
            "You are given a reference to a node in a connected undirected graph.",
            "Return a deep copy of the entire graph.",
        ],
        "examples": [
            "Input: adjacency = [[2, 4], [1, 3], [2, 4], [1, 3]]",
            "Output: a deep-copied graph with the same structure",
            "Input: adjacency = [[]]",
            "Output: a single copied node",
        ],
        "starter": """
class Solution:
    def solve(self, node: Node | None) -> Node | None:
        pass
""",
    },
    {
        "filename": "case21_nearest_sites.py",
        "title": "Nearest Sites",
        "prompt": [
            "Given a list of points on a plane, return the k points closest to the origin.",
            "You may return the answer in any order.",
        ],
        "examples": [
            "Input: points = [[1, 3], [-2, 2]], k = 1",
            "Output: [[-2, 2]]",
            "Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2",
            "Output: any two closest points",
        ],
        "starter": """
class Solution:
    def solve(self, points: list[list[int]], k: int) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case22_common_items.py",
        "title": "Common Items",
        "prompt": [
            "Return the k values that appear most often in the array.",
            "You may return them in any order.",
        ],
        "examples": [
            "Input: nums = [1, 1, 1, 2, 2, 3], k = 2",
            "Output: [1, 2]",
            "Input: nums = [1], k = 1",
            "Output: [1]",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        pass
""",
    },
    {
        "filename": "case23_sorted_stream_merge.py",
        "title": "Sorted Stream Merge",
        "support": LIST_NODE,
        "prompt": [
            "You are given k linked lists, each already sorted in ascending order.",
            "Merge them into one sorted linked list and return its head.",
        ],
        "examples": [
            "Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]",
            "Output: [1, 1, 2, 3, 4, 4, 5, 6]",
            "Input: lists = []",
            "Output: []",
        ],
        "starter": """
class Solution:
    def solve(self, lists: list[ListNode | None]) -> ListNode | None:
        pass
""",
    },
    {
        "filename": "case24_insert_schedule.py",
        "title": "Insert Schedule",
        "prompt": [
            "You are given a list of non-overlapping intervals sorted by start time.",
            "Insert one new interval and merge if needed so the result remains non-overlapping and sorted.",
        ],
        "examples": [
            "Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]",
            "Output: [[1, 5], [6, 9]]",
            "Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]",
            "Output: [[1, 2], [3, 10], [12, 16]]",
        ],
        "starter": """
class Solution:
    def solve(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case25_collapse_ranges.py",
        "title": "Collapse Ranges",
        "prompt": [
            "Given a list of intervals, merge all overlapping ranges.",
        ],
        "examples": [
            "Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]",
            "Output: [[1, 6], [8, 10], [15, 18]]",
            "Input: intervals = [[1, 4], [4, 5]]",
            "Output: [[1, 5]]",
        ],
        "starter": """
class Solution:
    def solve(self, intervals: list[list[int]]) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case26_keep_most_ranges.py",
        "title": "Keep Most Ranges",
        "prompt": [
            "Given a list of intervals, remove the fewest intervals so the remaining ones do not overlap.",
            "Return the number removed.",
        ],
        "examples": [
            "Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]",
            "Output: 1",
            "Input: intervals = [[1, 2], [1, 2], [1, 2]]",
            "Output: 2",
        ],
        "starter": """
class Solution:
    def solve(self, intervals: list[list[int]]) -> int:
        pass
""",
    },
    {
        "filename": "case27_wait_for_warmer.py",
        "title": "Wait For Warmer",
        "prompt": [
            "For each day, return how many days must pass until a warmer temperature occurs.",
            "If no warmer day exists, return 0 for that position.",
        ],
        "examples": [
            "Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]",
            "Output: [1, 1, 4, 2, 1, 1, 0, 0]",
            "Input: temperatures = [30, 40, 50, 60]",
            "Output: [1, 1, 1, 0]",
        ],
        "starter": """
class Solution:
    def solve(self, temperatures: list[int]) -> list[int]:
        pass
""",
    },
    {
        "filename": "case28_widest_histogram_block.py",
        "title": "Widest Histogram Block",
        "prompt": [
            "A histogram is represented by bar heights where each bar has width 1.",
            "Return the area of the largest rectangle that can be formed.",
        ],
        "examples": [
            "Input: heights = [2, 1, 5, 6, 2, 3]",
            "Output: 10",
            "Input: heights = [2, 4]",
            "Output: 4",
        ],
        "starter": """
class Solution:
    def solve(self, heights: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case29_zero_sum_triples.py",
        "title": "Zero Sum Triples",
        "prompt": [
            "Return all unique triplets [a, b, c] such that a + b + c == 0.",
            "Do not include duplicate triplets.",
        ],
        "examples": [
            "Input: nums = [-1, 0, 1, 2, -1, -4]",
            "Output: [[-1, -1, 2], [-1, 0, 1]]",
            "Input: nums = [0, 1, 1]",
            "Output: []",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        pass
""",
    },
    {
        "filename": "case30_water_between_walls.py",
        "title": "Water Between Walls",
        "prompt": [
            "Each array value is a wall height with width 1.",
            "After raining, compute how much water is trapped between the walls.",
        ],
        "examples": [
            "Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]",
            "Output: 6",
            "Input: height = [4, 2, 0, 3, 2, 5]",
            "Output: 9",
        ],
        "starter": """
class Solution:
    def solve(self, height: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case31_pack_nonzero.py",
        "title": "Pack Nonzero",
        "prompt": [
            "Move every zero in the array to the end while preserving the relative order of non-zero elements.",
            "Modify the array in place.",
        ],
        "examples": [
            "Input: nums = [0, 1, 0, 3, 12]",
            "Output: [1, 3, 12, 0, 0]",
            "Input: nums = [0]",
            "Output: [0]",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> None:
        pass
""",
    },
    {
        "filename": "case32_safe_night_loot.py",
        "title": "Safe Night Loot",
        "prompt": [
            "You plan to rob houses along a street.",
            "Adjacent houses cannot both be robbed.",
            "Return the maximum money you can collect.",
        ],
        "examples": [
            "Input: nums = [1, 2, 3, 1]",
            "Output: 4",
            "Input: nums = [2, 7, 9, 3, 1]",
            "Output: 12",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case33_low_cost_grid.py",
        "title": "Low Cost Grid",
        "prompt": [
            "Each cell contains a non-negative cost.",
            "Starting at the top-left and moving only right or down, return the minimum total cost to reach the bottom-right cell.",
        ],
        "examples": [
            "Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]",
            "Output: 7",
            "Input: grid = [[1, 2, 3], [4, 5, 6]]",
            "Output: 12",
        ],
        "starter": """
class Solution:
    def solve(self, grid: list[list[int]]) -> int:
        pass
""",
    },
    {
        "filename": "case34_peak_product_run.py",
        "title": "Peak Product Run",
        "prompt": [
            "Return the largest product obtainable from a contiguous subarray.",
        ],
        "examples": [
            "Input: nums = [2, 3, -2, 4]",
            "Output: 6",
            "Input: nums = [-2, 0, -1]",
            "Output: 0",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case35_best_gain_segment.py",
        "title": "Best Gain Segment",
        "prompt": [
            "Return the largest possible sum of a contiguous subarray.",
        ],
        "examples": [
            "Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]",
            "Output: 6",
            "Input: nums = [1]",
            "Output: 1",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case36_looped_best_segment.py",
        "title": "Looped Best Segment",
        "prompt": [
            "Treat the array as circular, so the subarray may wrap from the end back to the front.",
            "Return the maximum possible contiguous subarray sum.",
        ],
        "examples": [
            "Input: nums = [1, -2, 3, -2]",
            "Output: 3",
            "Input: nums = [5, -3, 5]",
            "Output: 10",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case37_one_skip_best_segment.py",
        "title": "One Skip Best Segment",
        "prompt": [
            "Return the largest sum of a non-empty subarray if you may delete at most one element from that chosen subarray.",
        ],
        "examples": [
            "Input: nums = [1, -2, 0, 3]",
            "Output: 4",
            "Input: nums = [1, -2, -2, 3]",
            "Output: 3",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case38_rising_trace.py",
        "title": "Rising Trace",
        "prompt": [
            "Return the length of the longest strictly increasing subsequence.",
            "The subsequence does not need to be contiguous.",
        ],
        "examples": [
            "Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]",
            "Output: 4",
            "Input: nums = [7, 7, 7, 7, 7, 7, 7]",
            "Output: 1",
        ],
        "starter": """
class Solution:
    def solve(self, nums: list[int]) -> int:
        pass
""",
    },
    {
        "filename": "case39_fewest_coins.py",
        "title": "Fewest Coins",
        "prompt": [
            "Given coin denominations and a target amount, return the fewest coins needed to make that amount.",
            "Return -1 if it cannot be formed.",
        ],
        "examples": [
            "Input: coins = [1, 2, 5], amount = 11",
            "Output: 3",
            "Input: coins = [2], amount = 3",
            "Output: -1",
        ],
        "starter": """
class Solution:
    def solve(self, coins: list[int], amount: int) -> int:
        pass
""",
    },
    {
        "filename": "case40_board_word_hunt.py",
        "title": "Board Word Hunt",
        "prompt": [
            "Given a grid of letters and a dictionary, return every word that can be formed by walking horizontally or vertically through adjacent cells.",
            "A cell may be used at most once per word.",
        ],
        "examples": [
            "Input: board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], words = ['oath','pea','eat','rain']",
            "Output: ['eat', 'oath']",
            "Input: board = [['a','b'],['c','d']], words = ['abcb']",
            "Output: []",
        ],
        "starter": """
class Solution:
    def solve(self, board: list[list[str]], words: list[str]) -> list[str]:
        pass
""",
    },
]


def render(spec: dict[str, str | list[str]]) -> str:
    lines = [
        "from __future__ import annotations",
        "",
        f"# {spec['title']}",
        "#",
    ]

    for line in spec["prompt"]:
        lines.append(f"# {line}")

    lines.append("#")

    for line in spec["examples"]:
        lines.append(f"# {line}")

    lines.append("")

    support = spec.get("support")
    if support:
        lines.append(dedent(support).strip())
        lines.append("")
        lines.append("")

    lines.append(dedent(spec["starter"]).strip())
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)

    readme_lines = [
        "# Review Set",
        "",
        "These files are intentionally renamed and reworded so you can practice the same core problems without relying on the original titles.",
        "",
        "Open any file in this folder and implement the stub from scratch.",
        "",
        "Files:",
    ]

    for spec in SPECS:
        content = render(spec)
        path = REVIEW_DIR / spec["filename"]
        path.write_text(content)
        readme_lines.append(f"- {spec['filename']}")

    (REVIEW_DIR / "README.md").write_text("\n".join(readme_lines) + "\n")


if __name__ == "__main__":
    main()
