class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store traversed elements in a dict
        pr = {nums[0]: 0}
        for i in range(len(nums)-1):
            idx = i+1
            addent = target - nums[idx]
            if addent in pr:
                return [pr[addent], idx]
            pr[nums[idx]] = idx
        return []
