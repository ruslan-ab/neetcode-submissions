class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        
        res = []
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if (nums[i], nums[j], nums[k]) not in res:
                            res.append((nums[i], nums[j], nums[k]))
        
        final_res = []
        for el in res:
            final_res.append(list(el))
        '''

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            el = nums[i]
            L = i + 1
            R = len(nums) - 1

            while L < R:
                sum = el + nums[L] + nums[R]
                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    res.append([el, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return res