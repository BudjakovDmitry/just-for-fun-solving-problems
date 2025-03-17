# Divide array into equal pairs

__Difficulty__: easy

## Description

You are given an integer array `nums` consisting of `2 * n` integers. You need to divide
`nums` into `n` pairs such that:

* each element belongs to exactly one pair;
* The elements present in a pair are equal.

Return `true` if nums can be divided into `n` pairs, otherwise return `false`.

## Example

### Example 1

__Input__: nums = [3,2,3,2,2,2]

__Output__: true

__Explanation__: There are 6 elements in `nums`, so they should be divided into
`6 / 2 = 3` pairs. If nums is divided into the pairs `(2, 2), (3, 3)`, and `(2, 2)`, it
will satisfy all the conditions.

### Example 2

__Input__: nums = [1,2,3,4]

__Output__: false

__Explanation__: There is no way to divide nums into `4 / 2 = 2` pairs such that the
pairs satisfy every condition.

## Constraints

* `nums.length == 2 * n`
* `1 <= n <= 500`
* `1 <= nums[i] <= 500`
