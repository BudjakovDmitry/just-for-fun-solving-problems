# Maximum count of positive integer and negative integer

__Difficulty__: easy

## Description

Given an array `nums` sorted in __non-decreasing__ order, return the _maximum between
the number of positive integers and the number of negative integers_.

In other words, if the number of positive integers in `nums` is `pos` and the number of
negative integers is `neg`, then return the maximum of `pos` and `neg`.

Note that `0` is neither positive nor negative.

## Examples

### Example 1

__Input__: `nums = [-2,-1,-1,1,2,3]`

__Output__: `3`

__Explanation__: There are 3 positive integers and 3 negative integers. The maximum
count among them is 3.

### Example 2

__Input__: `nums = [-3,-2,-1,0,0,1,2]`

__Output__: `3`

__Explanation__: There are 2 positive integers and 3 negative integers. The maximum
count among them is 3.

### Example 3

__Input__: `nums = [5,20,66,1314]`

__Output__: `4`

__Explanation__: There are 4 positive integers and 0 negative integers. The maximum
count among them is 4.

## Constraints

* `1 <= nums.length <= 2000`;
* `-2000 <= nums[i] <= 2000`;
* `nums` is sorted in a non-decreasing order.
