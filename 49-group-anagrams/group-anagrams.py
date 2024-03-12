class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            newMap = {}
            for letter in s:
                if letter in newMap:
                    newMap[letter] = newMap[letter] + 1
                else:
                    newMap[letter] = 1
            #print(newMap)
            if frozenset(newMap.items()) in hm:
                #print(f"{newMap} is in {hm}")
                hm[frozenset(newMap.items())].extend([s])
            else:
                hm[frozenset(newMap.items())] = [s]
        
        return hm.values()