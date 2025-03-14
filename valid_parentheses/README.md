# Valid Parentheses

__Difficulty__: easy

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and
`']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1

__Input__: s = "()"

__Output__: true

### Example 2

__Input__: s = "()[]{}"

__Output__: true

### Example 3

__Input__: s = "(]"

__Output__: false

### Example 4

__Input__: s = "([])"

__Output__: true

## Constraints

* 1 <= s.length <= 1e4;
* s consists of parentheses only `'()[]{}'`.
