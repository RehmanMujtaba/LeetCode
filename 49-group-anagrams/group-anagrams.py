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
            if json.dumps(newMap, sort_keys=True) in hm:
                #print(f"{newMap} is in {hm}")
                hm[json.dumps(newMap, sort_keys=True)].extend([s])
            else:
                hm[json.dumps(newMap, sort_keys=True)] = [s]
        
        return hm.values()