class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for n, c in counts.items():
            freq[c].append(n)

        res = []
        for c in range(len(freq)-1, 0, -1):
            for n in freq[c]:
                res.append(n)
                if len(res)==k:
                    return res

        return res