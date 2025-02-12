# 3450. Maximum students on a single bench

## Description

You are given a 2D integer array of student data `students`, where
`students[i] = [student_id, bench_id]` represents that student `student_id` is sitting
on the bench `bench_id`.

Return the __maximum__ number of _unique_ students sitting on any single bench. If no
students are present, return 0.

__Note__: A student can appear multiple times on the same bench in the input, but they
should be counted only once per bench.

## Examples

### Example 1:

__Input__: students = `[[1,2],[2,2],[3,3],[1,3],[2,3]]`

__Output__: 3

__Explanation:__

- Bench 2 has two unique students: `[1, 2]`.
- Bench 3 has three unique students: `[1, 2, 3]`.
- The maximum number of unique students on a single bench is 3.

### Example 2:

__Input__: students = `[[1,1],[2,1],[3,1],[4,2],[5,2]]`

__Output__: 3

__Explanation__:

- Bench 1 has three unique students: `[1, 2, 3]`.
- Bench 2 has two unique students: `[4, 5]`.
- The maximum number of unique students on a single bench is 3.

### Example 3:

__Input__: students = `[[1,1],[1,1]]`

__Output__: 1

__Explanation__:

The maximum number of unique students on a single bench is 1.

### Example 4:

__Input__: students = []

__Output__: 0

__Explanation__:

Since no students are present, the output is 0.

## Constraints

- `0 <= students.length <= 100`
- `students[i] = [student_id, bench_id]`
- `1 <= student_id <= 100`
- `1 <= bench_id <= 100`
