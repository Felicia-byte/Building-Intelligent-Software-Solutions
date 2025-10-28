#!/usr/bin/env python3
"""
Task 1: AI-Powered Code Completion
- Provides:
  1) An "AI-suggested" implementation (simulated) of sorting a list of dicts by a key.
  2) A manual implementation.
  3) A small benchmark and a 200-word analysis printed to stdout.

Note: For demonstration we simulate the AI-suggested code (as if produced by Copilot).
Compare readability and efficiency.
"""

import time
import random
import string
import copy
from typing import List, Dict, Any

# Generate sample data: list of dictionaries with 'priority' and other keys
def generate_sample(n=10000):
    rng = random.Random(42)
    data = []
    for i in range(n):
        data.append({
            "id": i,
            "name": ''.join(rng.choices(string.ascii_letters, k=8)),
            "priority": rng.randint(1, 1000),  # numeric key to sort by
        })
    return data

# -------------------------
# AI-suggested implementation (simulated)
# -------------------------
def ai_suggested_sort(dicts: List[Dict[str, Any]], key: str, reverse: bool = False):
    """
    AI-suggested approach (typical Copilot suggestion):
    Uses Python's built-in sorted with a lambda extractor.
    This is concise and idiomatic.
    Time complexity: O(n log n).
    """
    return sorted(dicts, key=lambda d: d.get(key, 0), reverse=reverse)

# -------------------------
# Manual implementation
# -------------------------
def manual_sort(dicts: List[Dict[str, Any]], key: str, reverse: bool = False):
    """
    Manual approach:
    - Extract (key, item) pairs
    - Use list.sort on pairs
    - Reconstruct list
    This demonstrates an explicit approach and allows stability control.
    """
    pairs = []
    for item in dicts:
        # Default to 0 if key missing (same behavior as ai_suggested)
        pairs.append((item.get(key, 0), item))
    # sort pairs in-place
    pairs.sort(reverse=reverse, key=lambda x: x[0])
    return [p[1] for p in pairs]

# -------------------------
# Benchmark function
# -------------------------
def benchmark():
    data = generate_sample(20000)  # adjust for machine capability
    # Use copies so each method sorts the same initial order
    a = copy.deepcopy(data)
    b = copy.deepcopy(data)

    t0 = time.time()
    _ = ai_suggested_sort(a, 'priority')
    t_ai = time.time() - t0

    t0 = time.time()
    _ = manual_sort(b, 'priority')
    t_manual = time.time() - t0

    print(f"AI-suggested sort time:   {t_ai:.4f} s")
    print(f"Manual sort time:         {t_manual:.4f} s")

    # Quick correctness check
    ai_res = ai_suggested_sort(data, 'priority')
    manual_res = manual_sort(data, 'priority')
    assert [d['id'] for d in ai_res] == [d['id'] for d in manual_res], "Results differ!"

    # 200-word analysis (approx)
    analysis = (
        "Analysis (≈200 words):\n"
        "The AI-suggested implementation uses Python's built-in sorted() with a lambda to "
        "extract the sort key. This approach is concise, idiomatic, and leverages the "
        "highly-optimized Timsort algorithm underlying Python's sort, giving O(n log n) "
        "time complexity and stability for equal keys. It avoids extra memory overhead beyond "
        "the temporary structures Python uses for sorting. The manual implementation creates "
        "an explicit list of (key, item) pairs, sorts them, and reconstructs the sorted list. "
        "This mirrors the decorate-sort-undecorate (Schwartzian transform) pattern and also "
        "runs in O(n log n), but it uses additional memory to hold the pairs and requires "
        "explicit reconstruction. In benchmark tests both methods perform similarly, with "
        "tiny differences dependent on data size and Python implementation details. For "
        "readability and maintainability, the AI-suggested sorted(...) variant is preferable "
        "because it's shorter and expresses intent directly; it's also what most Python "
        "developers expect. The manual variant can be useful when a custom extraction or "
        "precomputation of keys yields measurable speedups for expensive key functions."
    )
    print("\n" + analysis)

if __name__ == "__main__":
    benchmark()