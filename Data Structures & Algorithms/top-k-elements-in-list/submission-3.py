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


    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topF = dict()
        for n in nums:
            if n in topF:
                topF[n] += 1
            else:
                topF[n] = 1
        
        fr = sorted(list(topF.values()), reverse=True)
        res = []
        for i in range(k):
            cnt = fr[i]
            for num, c in topF.items():
                if c >= cnt:
                    res.append(num)
                    if len(res) == k:
                        return res
        
        return res
        '''