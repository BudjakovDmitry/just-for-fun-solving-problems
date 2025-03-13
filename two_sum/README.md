# Two sum

__Difficulty__: easy

## Description

Given an array of integers `nums` and an integer `target`, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

## Examples

### Example 1

__Input__: nums = [2,7,11,15], target = 9

__Output__: [0,1]

__Explanation__: Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2

__Input__: nums = [3,2,4], target = 6

__Output__: [1,2]

## Example 3

__Input__: nums = [3,3], target = 6

__Output__: [0,1]

## Constraints

* 2 <= nums.length <= 1e4;
* -1e9 <= nums[i] <= 1e;
* -1e9 <= target <= 1e9;
* only one valid answer exists.
