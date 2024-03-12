class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            newMap = {}
            for letter in s:
                newMap[letter] = newMap.get(letter, 1) + 1                
            theHash = hash(frozenset(newMap.items()))
            if theHash in hm:
                hm[theHash].append(s)
            else:
                hm[theHash] = [s]
        
        return hm.values()