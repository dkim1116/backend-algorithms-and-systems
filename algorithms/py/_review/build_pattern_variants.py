from __future__ import annotations

import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "pattern_variants"


SPECS: list[dict[str, object]] = [
    {
        "pattern": "arrays",
        "description": [
            "Given an unsorted integer array, return the smallest positive integer that does not appear in the array.",
            "Your solution should use linear time and constant extra space.",
        ],
        "examples": [
            "Input: nums = [1, 2, 0]",
            "Output: 3",
            "Input: nums = [3, 4, -1, 1]",
            "Output: 2",
            "Input: nums = [7, 8, 9, 11, 12]",
            "Output: 1",
        ],
        "constraints": [
            "1 <= len(nums) <= 10^5",
            "-2^31 <= nums[i] <= 2^31 - 1",
            "Aim for O(n) time and O(1) extra space.",
        ],
    },
    {
        "pattern": "hashing",
        "description": [
            "Given a binary array, return the length of the longest contiguous subarray with an equal number of zeros and ones.",
        ],
        "examples": [
            "Input: nums = [0, 1]",
            "Output: 2",
            "Input: nums = [0, 1, 0]",
            "Output: 2",
        ],
        "constraints": [
            "1 <= len(nums) <= 10^5",
            "nums[i] is either 0 or 1.",
        ],
    },
    {
        "pattern": "binary_search",
        "description": [
            "Two sorted arrays are given.",
            "Return the median of the combined multiset in logarithmic time with respect to the smaller array.",
        ],
        "examples": [
            "Input: nums1 = [1, 3], nums2 = [2]",
            "Output: 2.0",
            "Input: nums1 = [1, 2], nums2 = [3, 4]",
            "Output: 2.5",
        ],
        "constraints": [
            "0 <= len(nums1), len(nums2) <= 1000",
            "1 <= len(nums1) + len(nums2) <= 2000",
            "-10^6 <= nums1[i], nums2[i] <= 10^6",
            "Aim for O(log(min(m, n))) time.",
        ],
    },
    {
        "pattern": "sliding_window",
        "description": [
            "You are given a string and a list of words where every word has the same length.",
            "Return every starting index where a substring can be formed by concatenating each word exactly once and without extra characters between them.",
            "The answer may be returned in any order.",
        ],
        "examples": [
            "Input: s = 'barfoothefoobarman', words = ['foo', 'bar']",
            "Output: [0, 9]",
            "Input: s = 'wordgoodgoodgoodbestword', words = ['word', 'good', 'best', 'good']",
            "Output: [8]",
        ],
        "constraints": [
            "1 <= len(s) <= 10^4",
            "1 <= len(words) <= 5000",
            "1 <= len(words[0]) <= 30",
            "All words have the same length.",
        ],
    },
    {
        "pattern": "backtracking",
        "description": [
            "Place n queens on an n x n chessboard so that no two queens attack each other.",
            "Return all valid board configurations.",
        ],
        "examples": [
            "Input: n = 4",
            "Output: [['.Q..','...Q','Q...','..Q.'], ['..Q.','Q...','...Q','.Q..']]",
            "Input: n = 1",
            "Output: [['Q']]",
        ],
        "constraints": [
            "1 <= n <= 9",
            "Each returned board must contain exactly n queens.",
        ],
    },
    {
        "pattern": "trees",
        "description": [
            "Design two functions for a binary tree:",
            "one that converts the tree into a string representation, and one that rebuilds the same tree from that representation.",
            "Your format may be any deterministic format that preserves the exact structure and values.",
        ],
        "examples": [
            "Input: root = [1, 2, 3, null, null, 4, 5]",
            "Output: deserializing the serialized form reconstructs the same tree",
            "Input: root = []",
            "Output: deserializing the serialized form reconstructs the same empty tree",
        ],
        "constraints": [
            "0 <= number of nodes <= 10^4",
            "-1000 <= node.val <= 1000",
            "Preserve exact structure, not just values.",
        ],
    },
    {
        "pattern": "graphs",
        "description": [
            "A sorted dictionary from an unknown language is given as a list of words already in lexicographic order for that language.",
            "Return one valid ordering of the letters.",
            "If no valid ordering exists, return an empty string.",
        ],
        "examples": [
            "Input: words = ['wrt', 'wrf', 'er', 'ett', 'rftt']",
            "Output: 'wertf'",
            "Input: words = ['z', 'x', 'z']",
            "Output: ''",
        ],
        "constraints": [
            "1 <= len(words) <= 100",
            "1 <= len(words[i]) <= 100",
            "All words consist of lowercase English letters.",
        ],
    },
    {
        "pattern": "heaps",
        "description": [
            "You are given multiple sorted lists of integers.",
            "Return the smallest inclusive range [a, b] such that the range contains at least one number from each list.",
            "If multiple ranges have the same width, prefer the one with the smaller start.",
        ],
        "examples": [
            "Input: nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]",
            "Output: [20, 24]",
        ],
        "constraints": [
            "1 <= number of lists <= 3500",
            "1 <= len(nums[i]) <= 50",
            "-10^5 <= nums[i][j] <= 10^5",
            "Each individual list is sorted in nondecreasing order.",
        ],
    },
    {
        "pattern": "intervals",
        "description": [
            "Each employee has a sorted list of non-overlapping working intervals.",
            "Return all finite intervals where every employee is free.",
        ],
        "examples": [
            "Input: schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]",
            "Output: [[3, 4]]",
            "Input: schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]",
            "Output: [[5, 6], [7, 9]]",
        ],
        "constraints": [
            "1 <= number of employees <= 50",
            "1 <= number of intervals per employee <= 50",
            "Each employee's intervals are sorted and non-overlapping.",
        ],
    },
    {
        "pattern": "monotonic_stack",
        "description": [
            "Return the sum of the minimum value of every contiguous subarray.",
            "Because the answer may be large, return it modulo 10^9 + 7.",
        ],
        "examples": [
            "Input: arr = [3, 1, 2, 4]",
            "Output: 17",
            "Input: arr = [11, 81, 94, 43, 3]",
            "Output: 444",
        ],
        "constraints": [
            "1 <= len(arr) <= 3 * 10^4",
            "1 <= arr[i] <= 3 * 10^4",
        ],
    },
    {
        "pattern": "dynamic_programming",
        "description": [
            "Given a list of positive integers, determine whether it can be split into two subsets whose sums are equal.",
        ],
        "examples": [
            "Input: nums = [1, 5, 11, 5]",
            "Output: True",
            "Input: nums = [1, 2, 3, 5]",
            "Output: False",
        ],
        "constraints": [
            "1 <= len(nums) <= 200",
            "1 <= nums[i] <= 100",
        ],
    },
    {
        "pattern": "trie",
        "description": [
            "Design a word dictionary that supports two operations:",
            "adding a word, and searching whether a pattern matches any inserted word.",
            "The search pattern may contain the '.' character, which matches any single lowercase letter.",
        ],
        "examples": [
            "Input: addWord('bad'), addWord('dad'), addWord('mad'), search('pad'), search('bad'), search('.ad'), search('b..')",
            "Output: [None, None, None, False, True, True, True]",
        ],
        "constraints": [
            "1 <= word length <= 25",
            "Words and patterns consist of lowercase English letters and '.' in search patterns.",
            "At most 10^4 calls will be made in total.",
        ],
    },
    {
        "pattern": "union_find",
        "description": [
            "A sequence of undirected edges is added one by one to a graph whose nodes are labeled from 1 to n.",
            "Exactly one added edge creates a cycle in what was otherwise a tree-like structure.",
            "Return the edge that can be removed so the remaining edges form a valid tree again.",
            "If multiple answers are possible, return the one that appears last in the input.",
        ],
        "examples": [
            "Input: edges = [[1, 2], [1, 3], [2, 3]]",
            "Output: [2, 3]",
            "Input: edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]",
            "Output: [1, 4]",
        ],
        "constraints": [
            "3 <= len(edges) <= 1000",
            "Each edge has length 2.",
            "1 <= u, v <= len(edges)",
            "The graph is connected after all edges are added.",
        ],
    },
]


def render(spec: dict[str, object]) -> str:
    description = spec["description"]
    examples = spec["examples"]
    constraints = spec["constraints"]

    lines = ["# Description"]
    lines.extend(f"# {line}" for line in description)  # type: ignore[arg-type]
    lines.append("#")
    lines.append("# Examples")
    lines.extend(f"# {line}" for line in examples)  # type: ignore[arg-type]
    lines.append("#")
    lines.append("# Constraints")
    lines.extend(f"# - {line}" for line in constraints)  # type: ignore[arg-type]
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for existing in OUT_DIR.glob("*.py"):
        existing.unlink()

    shuffler = random.SystemRandom()
    shuffled = shuffler.sample(SPECS, k=len(SPECS))

    for index, spec in enumerate(shuffled, start=1):
        filename = f"{index:03d}.py"
        (OUT_DIR / filename).write_text(render(spec))


if __name__ == "__main__":
    main()
