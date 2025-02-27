# 2769. Find the Maximum Achievable Number


__Difficulty:__ easy

## Description

Given two integers, `num` and `t`. A number `x` is achievable if it can become equal to
`num` after applying the following operation at most `t` times:

Increase or decrease `x` by `1`, and _simultaneously_ increase or decrease `num` by `1`.

Return the maximum possible value of `x`.

## Examples

### Example 1

__Input__: num = 4, t = 1

__Output__: 6

__Explanation__:

Apply the following operation once to make the maximum achievable number equal to `num`:

Decrease the maximum achievable number by `1`, and increase `num` by `1`.

### Example 2

__Input__: num = 3, t = 2

__Output__: 7

__Explanation__:

Apply the following operation twice to make the maximum achievable number equal to
`num`:

Decrease the maximum achievable number by `1`, and increase `num` by `1`.

## Constraints

- `1 <= num`
- `t <= 50`
