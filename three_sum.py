#!/venv/bin/python3

"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

def threeSum(nums: list[int]) -> list[list[int]]:

    triplets = []

    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
    
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                triplets.append([nums[left], nums[i], nums[right]])

                # skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    

    return triplets

print(threeSum([-1,0,1,2,-1,-4]))

