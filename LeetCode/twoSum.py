def twoSum(nums, target):
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]

assert twoSum([1, 1], 2) == [0, 1]
assert twoSum([1, 1, 1], 2) == [0, 1]

assert twoSum([2, 1, 1, 1], 2) == [1, 2]
