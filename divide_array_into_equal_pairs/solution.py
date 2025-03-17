def divide_array(nums: list[int]) -> bool:
    values = set()
    for n in nums:
        if n not in values:
            values.add(n)
        else:
            values.remove(n)
    return not bool(values)
