#!/venv/bin/python3

"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    if not nums:
        return 0
    
    res = len(nums) + 1
    current_sum = 0
    left = 0

    for right, n in enumerate(nums):
        current_sum += n
        while current_sum >= target and left <= right:
            res = min(res, (right - left) + 1)
            current_sum -= nums[left]
            left += 1

    return res%(len(nums) + 1)


minSubArrayLen(11, [1,2,3,4,5])

#input = target = 7, nums = [2,3,1,2,4,3]