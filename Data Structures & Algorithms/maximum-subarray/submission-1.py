class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum