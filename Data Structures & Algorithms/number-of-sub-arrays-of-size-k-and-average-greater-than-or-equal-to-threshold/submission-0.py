class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curr_sum = sum(arr[L:k-1])
        cnt = 0

        for R in range(k-1, len(arr)):
            curr_sum += arr[R]
            
            if curr_sum >= threshold * k:
                cnt += 1
            
            curr_sum -= arr[L]
            L += 1
        return cnt
