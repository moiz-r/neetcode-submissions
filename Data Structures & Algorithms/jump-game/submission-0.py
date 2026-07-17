class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        farthest = 0
        n = len(nums) - 1

        for i in range(n+1):
            if i > farthest: # if i is greater than Farthest we could reach from last jump
                return False 
            farthest = max(farthest, i + nums[i])
            
            if farthest >= n:
                return True 


            