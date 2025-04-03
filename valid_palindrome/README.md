# Valid Palindrome

__Difficulty__: easy

## Description

A phrase is a _palindrome_ if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a _palindrome_, or `false` otherwise.

## Examples

### Example 1

__Input__: s = "A man, a plan, a canal: Panama"

__Output__: true

__Explanation__: "amanaplanacanalpanama" is a palindrome.

### Example 2

__Input__: s = "race a car"

__Output__: false

__Explanation__: "raceacar" is not a palindrome.

### Example 3

__Input__: s = " "

__Output__: true

__Explanation__: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

## Constraints

* `1 <= s.length <= 2 * 105`
* `s` consists only of printable ASCII characters.