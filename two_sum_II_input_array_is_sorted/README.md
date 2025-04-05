# Two Sum II - Input Array Is Sorted

__Difficulty__: medium

## Description

Given a 1-indexed array of integers `numbers` that is already __sorted in non-decreasing
order__, find two numbers such that they add up to a specific `target` number. Let these
two numbers be `numbers[index1]` and `numbers[index2]` where
`1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer
array `[index1, index2]` of length 2.

The tests are generated such that there is __exactly one solution__. You __may not__ use
the same element twice.

Your solution must use only constant extra space.

## Examples

### Example 1

__Input__: numbers = [2,7,11,15], target = 9

__Output__: [1,2]

__Explanation__: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return
[1, 2].

### Example 2

__Input__: numbers = [2,3,4], target = 6

__Output__: [1,3]

__Explanation__: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return
[1, 3].

## Constraints

* `2 <= numbers.length <= 3 * 10e3`
* `-1000 <= numbers[i] <= 1000`
* `numbers` is sorted in __non-decreasing order__.
* `-1000 <= target <= 1000`
* The tests are generated such that there is __exactly one solution__.
