from __future__ import annotations

import random
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
REVIEW_DIR = ROOT / "review"
MASKED_DIR = ROOT / "masked"


def parse_review_file(filename: str) -> tuple[list[str], list[str]]:
    path = REVIEW_DIR / filename
    comment_lines: list[str] = []

    for raw_line in path.read_text().splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("#"):
            comment_lines.append(stripped[1:].lstrip())

    if not comment_lines:
        raise ValueError(f"No comment prompt found in {filename}")

    body = comment_lines[1:]
    sections: list[list[str]] = []
    current: list[str] = []

    for line in body:
        if line == "":
            if current:
                sections.append(current)
                current = []
            continue
        current.append(line)

    if current:
        sections.append(current)

    if len(sections) < 2:
        raise ValueError(f"Prompt parsing failed for {filename}")

    description = sections[0]
    examples = sections[1]
    return description, examples


def generic_constraints(description: list[str]) -> list[str]:
    joined = " ".join(description).lower()
    constraints = [
        "Inputs follow the shapes shown in the examples.",
        "Return exactly the value, collection, or boolean requested.",
        "Assume the input size can be large enough that inefficient brute-force approaches may time out.",
    ]

    if any(word in joined for word in ["tree", "graph", "linked list", "linked lists"]):
        constraints.insert(1, "Use the standard node-based structure implied by the prompt when one is needed.")
    elif "grid" in joined or "matrix" in joined or "board" in joined:
        constraints.insert(1, "Preserve the row and column boundaries described by the prompt.")

    return constraints


CURATED_SPECS: list[dict[str, object]] = [
    {
        "description": [
            "You are given a sorted array of integers in ascending order and a target value.",
            "Return the index of the target if it exists, or -1 if it does not.",
            "Your solution should run in logarithmic time.",
        ],
        "examples": [
            "Input: nums = [-1, 0, 3, 5, 9, 12], target = 9",
            "Output: 4",
            "Input: nums = [-1, 0, 3, 5, 9, 12], target = 2",
            "Output: -1",
        ],
        "constraints": generic_constraints(
            [
                "You are given a sorted array of integers in ascending order and a target value.",
                "Return the index of the target if it exists, or -1 if it does not.",
                "Your solution should run in logarithmic time.",
            ]
        ),
    },
    {"source": "case01_shifted_lookup.py"},
    {
        "description": [
            "You are given a sorted array of integers and a target value.",
            "Return the first and last index where the target appears.",
            "If the target is absent, return [-1, -1].",
        ],
        "examples": [
            "Input: nums = [5, 7, 7, 8, 8, 10], target = 8",
            "Output: [3, 4]",
            "Input: nums = [5, 7, 7, 8, 8, 10], target = 6",
            "Output: [-1, -1]",
        ],
        "constraints": generic_constraints(
            [
                "You are given a sorted array of integers and a target value.",
                "Return the first and last index where the target appears.",
                "If the target is absent, return [-1, -1].",
            ]
        ),
    },
    {"source": "case02_load_balancer.py"},
    {
        "description": [
            "Packages must be shipped in the given order over exactly d days.",
            "Choose the smallest ship capacity that allows all packages to be delivered within the limit.",
        ],
        "examples": [
            "Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], d = 5",
            "Output: 15",
            "Input: weights = [3, 2, 2, 4, 1, 4], d = 3",
            "Output: 6",
        ],
        "constraints": generic_constraints(
            [
                "Packages must be shipped in the given order over exactly d days.",
                "Choose the smallest ship capacity that allows all packages to be delivered within the limit.",
            ]
        ),
    },
    {"source": "case03_bloom_deadline.py"},
    {"source": "case04_max_gap_placement.py"},
    {"source": "case05_tight_cover.py"},
    {"source": "case06_uniform_stretch.py"},
    {"source": "case07_hidden_anagram.py"},
    {"source": "case08_target_runs.py"},
    {"source": "case09_streak_length.py"},
    {
        "description": [
            "Return an array where each position contains the product of every other value in the input array.",
            "Do not use division.",
        ],
        "examples": [
            "Input: nums = [1, 2, 3, 4]",
            "Output: [24, 12, 8, 6]",
            "Input: nums = [-1, 1, 0, -3, 3]",
            "Output: [0, 0, 9, 0, 0]",
        ],
        "constraints": generic_constraints(
            [
                "Return an array where each position contains the product of every other value in the input array.",
                "Do not use division.",
            ]
        ),
    },
    {
        "description": [
            "Return every possible subset of the given distinct integers.",
            "The answer may be returned in any order.",
        ],
        "examples": [
            "Input: nums = [1, 2, 3]",
            "Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]",
            "Input: nums = [0]",
            "Output: [[], [0]]",
        ],
        "constraints": generic_constraints(
            [
                "Return every possible subset of the given distinct integers.",
                "The answer may be returned in any order.",
            ]
        ),
    },
    {"source": "case10_unlimited_recipe.py"},
    {"source": "case11_single_use_recipe.py"},
    {"source": "case12_full_arrangements.py"},
    {"source": "case13_best_branch_route.py"},
    {"source": "case14_tree_span.py"},
    {"source": "case15_shared_ancestor.py"},
    {"source": "case16_ordered_tree_check.py"},
    {"source": "case17_rank_in_ordered_tree.py"},
    {
        "description": [
            "Return the values of a binary tree level by level from top to bottom.",
            "Nodes on the same depth should appear together in the same inner list.",
        ],
        "examples": [
            "Input: root = [3, 9, 20, null, null, 15, 7]",
            "Output: [[3], [9, 20], [15, 7]]",
            "Input: root = [1]",
            "Output: [[1]]",
        ],
        "constraints": generic_constraints(
            [
                "Return the values of a binary tree level by level from top to bottom.",
                "Nodes on the same depth should appear together in the same inner list.",
            ]
        ),
    },
    {"source": "case18_dependency_finish.py"},
    {"source": "case19_land_clusters.py"},
    {"source": "case20_graph_copy.py"},
    {"source": "case21_nearest_sites.py"},
    {"source": "case22_common_items.py"},
    {"source": "case23_sorted_stream_merge.py"},
    {"source": "case24_insert_schedule.py"},
    {"source": "case25_collapse_ranges.py"},
    {"source": "case26_keep_most_ranges.py"},
    {
        "description": [
            "You are given a list of meeting time intervals.",
            "Return the minimum number of rooms required so that no meetings that overlap share a room.",
        ],
        "examples": [
            "Input: intervals = [[0, 30], [5, 10], [15, 20]]",
            "Output: 2",
            "Input: intervals = [[7, 10], [2, 4]]",
            "Output: 1",
        ],
        "constraints": generic_constraints(
            [
                "You are given a list of meeting time intervals.",
                "Return the minimum number of rooms required so that no meetings that overlap share a room.",
            ]
        ),
    },
    {
        "description": [
            "Design a booking structure for half-open time intervals [start, end).",
            "A booking is allowed only if no time is covered by three different bookings after the insertion.",
            "Return whether each booking can be accepted.",
        ],
        "examples": [
            "Input: book(10, 20), book(50, 60), book(10, 40), book(5, 15), book(5, 10), book(25, 55)",
            "Output: [True, True, True, False, True, True]",
        ],
        "constraints": generic_constraints(
            [
                "Design a booking structure for half-open time intervals [start, end).",
                "A booking is allowed only if no time is covered by three different bookings after the insertion.",
                "Return whether each booking can be accepted.",
            ]
        ),
    },
    {"source": "case27_wait_for_warmer.py"},
    {"source": "case28_widest_histogram_block.py"},
    {"source": "case29_zero_sum_triples.py"},
    {"source": "case30_water_between_walls.py"},
    {"source": "case31_pack_nonzero.py"},
    {"source": "case32_safe_night_loot.py"},
    {"source": "case33_low_cost_grid.py"},
    {"source": "case34_peak_product_run.py"},
    {"source": "case35_best_gain_segment.py"},
    {"source": "case36_looped_best_segment.py"},
    {"source": "case37_one_skip_best_segment.py"},
    {"source": "case38_rising_trace.py"},
    {"source": "case39_fewest_coins.py"},
    {"source": "case40_board_word_hunt.py"},
]


EXTRA_SPECS: list[dict[str, object]] = [
    {
        "description": [
            "Given a string, return the length of the longest substring that contains no repeated characters.",
        ],
        "examples": [
            "Input: s = 'abcabcbb'",
            "Output: 3",
            "Input: s = 'bbbbb'",
            "Output: 1",
        ],
        "constraints": generic_constraints(
            [
                "Given a string, return the length of the longest substring that contains no repeated characters.",
            ]
        ),
    },
    {
        "description": [
            "Given a text string and a pattern string, return every starting index where a permutation of the pattern appears in the text.",
            "The answer may be returned in any order.",
        ],
        "examples": [
            "Input: s = 'cbaebabacd', p = 'abc'",
            "Output: [0, 6]",
            "Input: s = 'abab', p = 'ab'",
            "Output: [0, 1, 2]",
        ],
        "constraints": generic_constraints(
            [
                "Given a text string and a pattern string, return every starting index where a permutation of the pattern appears in the text.",
                "The answer may be returned in any order.",
            ]
        ),
    },
    {
        "description": [
            "Return True if a binary tree is height-balanced.",
            "A tree is balanced when the heights of the two child subtrees of every node differ by at most one.",
        ],
        "examples": [
            "Input: root = [3, 9, 20, null, null, 15, 7]",
            "Output: True",
            "Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]",
            "Output: False",
        ],
        "constraints": generic_constraints(
            [
                "Return True if a binary tree is height-balanced.",
                "A tree is balanced when the heights of the two child subtrees of every node differ by at most one.",
            ]
        ),
    },
    {
        "description": [
            "Return the list of node values that would be visible when looking at a binary tree from the right side.",
            "Values should be reported from top level to bottom level.",
        ],
        "examples": [
            "Input: root = [1, 2, 3, null, 5, null, 4]",
            "Output: [1, 3, 4]",
            "Input: root = [1, null, 3]",
            "Output: [1, 3]",
        ],
        "constraints": generic_constraints(
            [
                "Return the list of node values that would be visible when looking at a binary tree from the right side.",
                "Values should be reported from top level to bottom level.",
            ]
        ),
    },
    {
        "description": [
            "A grid contains empty cells, fresh items, and rotten items.",
            "Every minute, any fresh item directly adjacent up, down, left, or right to a rotten one also becomes rotten.",
            "Return the minimum minutes needed for all fresh items to rot, or -1 if it is impossible.",
        ],
        "examples": [
            "Input: grid = [[2,1,1],[1,1,0],[0,1,1]]",
            "Output: 4",
            "Input: grid = [[2,1,1],[0,1,1],[1,0,1]]",
            "Output: -1",
        ],
        "constraints": generic_constraints(
            [
                "A grid contains empty cells, fresh items, and rotten items.",
                "Every minute, any fresh item directly adjacent up, down, left, or right to a rotten one also becomes rotten.",
                "Return the minimum minutes needed for all fresh items to rot, or -1 if it is impossible.",
            ]
        ),
    },
    {
        "description": [
            "Heights are given in a matrix.",
            "Water can flow from a cell to a neighboring cell with height less than or equal to the current cell.",
            "Return all coordinates from which water can reach both the top or left border and the bottom or right border.",
        ],
        "examples": [
            "Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]",
            "Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]",
        ],
        "constraints": generic_constraints(
            [
                "Heights are given in a matrix.",
                "Water can flow from a cell to a neighboring cell with height less than or equal to the current cell.",
                "Return all coordinates from which water can reach both the top or left border and the bottom or right border.",
            ]
        ),
    },
    {
        "description": [
            "Design a structure that supports adding numbers from a data stream and returning the median of all inserted numbers at any time.",
        ],
        "examples": [
            "Input: addNum(1), addNum(2), findMedian(), addNum(3), findMedian()",
            "Output: [None, None, 1.5, None, 2.0]",
        ],
        "constraints": generic_constraints(
            [
                "Design a structure that supports adding numbers from a data stream and returning the median of all inserted numbers at any time.",
            ]
        ),
    },
    {
        "description": [
            "Return the k-th largest value in an unsorted array.",
            "The answer should be the value that would appear in that position in descending order, not the k-th distinct value.",
        ],
        "examples": [
            "Input: nums = [3, 2, 1, 5, 6, 4], k = 2",
            "Output: 5",
            "Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4",
            "Output: 4",
        ],
        "constraints": generic_constraints(
            [
                "Return the k-th largest value in an unsorted array.",
                "The answer should be the value that would appear in that position in descending order, not the k-th distinct value.",
            ]
        ),
    },
]


def resolve_spec(spec: dict[str, object]) -> tuple[list[str], list[str], list[str]]:
    if "source" in spec:
        description, examples = parse_review_file(spec["source"])  # type: ignore[arg-type]
        constraints = generic_constraints(description)
        return description, examples, constraints

    description = spec["description"]  # type: ignore[assignment]
    examples = spec["examples"]  # type: ignore[assignment]
    constraints = spec["constraints"]  # type: ignore[assignment]
    return description, examples, constraints


def render_file(description: list[str], examples: list[str], constraints: list[str]) -> str:
    lines = ["# Description"]
    lines.extend(f"# {line}" for line in description)
    lines.append("#")
    lines.append("# Examples")
    lines.extend(f"# {line}" for line in examples)
    lines.append("#")
    lines.append("# Constraints")
    lines.extend(f"# - {line}" for line in constraints)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    MASKED_DIR.mkdir(parents=True, exist_ok=True)

    for existing in MASKED_DIR.glob("*.md"):
        existing.unlink()
    for existing in MASKED_DIR.glob("*.py"):
        existing.unlink()

    original_specs = CURATED_SPECS + EXTRA_SPECS
    shuffler = random.SystemRandom()
    all_specs = shuffler.sample(original_specs, k=len(original_specs))

    while all_specs[:6] == original_specs[:6]:
        all_specs = shuffler.sample(original_specs, k=len(original_specs))

    for index, spec in enumerate(all_specs, start=1):
        description, examples, constraints = resolve_spec(spec)
        filename = f"{index:03d}.py"
        (MASKED_DIR / filename).write_text(render_file(description, examples, constraints))


if __name__ == "__main__":
    main()
