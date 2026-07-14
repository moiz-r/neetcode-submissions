class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(n):
            if n == 0 or n == 1:
                return 1
            elif n in memo:
                return memo[n]
            else:
                ans =  ways(n-1) + ways(n-2)
                memo[n] = ans
                return ans
            
        return ways(n)

        