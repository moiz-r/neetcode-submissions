class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_ = nums[left] + nums[right]

            if sum_ ==  target:
                return [left + 1, right+1]
            if sum_ > target:
                right = right - 1

            else:
                left = left + 1
