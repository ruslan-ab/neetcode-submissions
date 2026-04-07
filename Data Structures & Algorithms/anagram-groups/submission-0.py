class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        oAnagrams = dict()
        for s in strs:
            o = self.getOrderedStr(s)
            if o in oAnagrams:
                oAnagrams[o].append(s)
            else:
                oAnagrams[o] = [s]
        return list(oAnagrams.values())

    def getOrderedStr(self, s: str) -> str:
        return "".join(sorted(s))