class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            #print(newMap)
            if sortedString in hm:
                #print(f"{newMap} is in {hm}")
                hm[sortedString].extend([s])
            else:
                hm[sortedString] = [s]
        
        return hm.values()