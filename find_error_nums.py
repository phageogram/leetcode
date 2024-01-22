#!/venv/bin/python3

def findErrorNums(nums):
        if not nums:
            return []
        
        correct_list = [x for x in range(1, len(nums) + 1)]
        l = []
        dup = 0
        missing = 0

        for i in nums:
            if nums.count(i) > 1:
                dup = i
                break
        
        for i in correct_list:
            if i not in nums:
                missing = i
                break
        
        l = [dup, missing]

        return l


print(findErrorNums([3,2,2]))
