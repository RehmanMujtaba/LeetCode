class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in hm:
                hm[sortedString].extend([s])
            else:
                hm[sortedString] = [s]
        
        return hm.values()