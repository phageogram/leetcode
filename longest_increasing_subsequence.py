#!/venv/bin/python3
"""
#This fails if nums = [0, 1, 0, 3, 2, 3] because it will return [0,1,3] as the longest increasing subsequence, rather than [0,1,2,3] like it should

def lengthOfLIS(nums: list[int]) -> int:
    pointer = 0
    sub_list = []

    while pointer < len(nums):
        temp = [nums[pointer]]

        for i in range(pointer + 1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
        sub_list.append(temp)
        pointer += 1
    return sub_list
    #return len(max(sub_list, key=len))


print(lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))

print(lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))"""

def lengthOfLIS(nums: list[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)

# Test case
print(lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))

# [1, 2, 1, 3, 3, 4]