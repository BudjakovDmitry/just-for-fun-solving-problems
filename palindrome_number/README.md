# Palindrome number

__Difficulty__: easy

## Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

> An integer is a palindrome when it reads the same forward and backward. For example,
> `121` is a palindrome while `123` is not.

## Examples

### Example 1

__Input__: x = 121

__Output__: true

__Explanation__: 121 reads as 121 from left to right and from right to left.

### Example 2

__Input__: x = -121

__Output__: false

__Explanation__: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore, it is not a palindrome.

### Example 3

__Input__: x = 10

__Output__: false

__Explanation__: Reads 01 from right to left. Therefore, it is not a palindrome.

## Constraints

-2^31 <= x <= 2^31 - 1
