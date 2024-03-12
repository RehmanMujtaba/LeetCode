class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            newMap = {}
            for letter in s:
                if letter in newMap:
                    newMap[letter] += 1
                else:
                    newMap[letter] = 1
            #print(newMap)
            hm[hash(frozenset(newMap.items()))] = hm.get(hash(frozenset(newMap.items())), []) + [s]
        
        return hm.values()