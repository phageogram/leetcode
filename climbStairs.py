#!/venv/bin/python3
"""You are climbing a staircase. It takes n steps to reach the top.
   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

def climbStairs(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    
    prev, curr = 1, 1

    for i in range(2, n+1):
        temp = curr
        curr = prev + curr
        prev = temp
        print(temp, prev, curr)
    return curr

print(climbStairs(45))

"""Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""