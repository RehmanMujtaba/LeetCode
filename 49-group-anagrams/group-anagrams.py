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
            theHash = hash(frozenset(newMap.items()))
            if theHash in hm:
                hm[theHash].append(s)
            else:
                hm[theHash] = [s]
        
        return hm.values()