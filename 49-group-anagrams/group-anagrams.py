class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            newMap = {}
            for letter in s:
                newMap[letter] = newMap.get(letter, 0) + 1
            theHash = hash(frozenset(newMap.items()))
            hm[theHash] = hm.get(theHash, []) + [s]
        
        return hm.values()