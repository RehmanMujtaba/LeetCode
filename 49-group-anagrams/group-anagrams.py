import hashlib
import base64

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        def make_hash_sha256(o):
            hasher = hashlib.sha256()
            hasher.update(repr(make_hashable(o)).encode())
            return base64.b64encode(hasher.digest()).decode()

        def make_hashable(o):
            if isinstance(o, (tuple, list)):
                return tuple((make_hashable(e) for e in o))

            if isinstance(o, dict):
                return tuple(sorted((k,make_hashable(v)) for k,v in o.items()))

            if isinstance(o, (set, frozenset)):
                return tuple(sorted(make_hashable(e) for e in o))

            return o

        hm = {}

        for s in strs:
            newMap = {}
            for letter in s:
                if letter in newMap:
                    newMap[letter] = newMap[letter] + 1
                else:
                    newMap[letter] = 1
            #print(newMap)
            if make_hashable(newMap) in hm:
                #print(f"{newMap} is in {hm}")
                hm[make_hashable(newMap)].extend([s])
            else:
                hm[make_hashable(newMap)] = [s]
        
        return hm.values()