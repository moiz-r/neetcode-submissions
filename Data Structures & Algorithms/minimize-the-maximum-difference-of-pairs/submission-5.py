class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        ans = []
        nums.sort()
        len_ = len(nums)
        l = 0 
        r = nums[-1] - nums[0]

        def canPair(threshold):
            count = 0
            i = 0
            while i < len_ - 1:
                diff = nums[i+1] - nums[i]

                if diff <= threshold:
                    count += 1
                    i += 2
                    if count == p:
                        return True
                else:
                    i += 1
            
            return count >= p
        
        while l < r:
            mid = (l +r) // 2
            
            if canPair(mid):
                r = mid
            else:
                l = mid + 1
            
        return l


