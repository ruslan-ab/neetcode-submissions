class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        res = ",".join(sizes)
        res = res + "#" + "".join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        delPos = s.find("#")
        sizesStr = s[0:delPos]
        sizes = sizesStr.split(",")
        
        res = []
        offset = delPos+1
        for size in sizes:
            res.append(s[offset:offset + int(size)])
            offset = offset + int(size)
        return res

