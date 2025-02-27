from collections import defaultdict
from typing import List


def max_students(students: List[List[int]]) -> int:
    benches = defaultdict(set)
    for student_id, bench_id in students:
        benches[bench_id].add(student_id)

    return max(len(v) for v in benches.values()) if benches else 0
