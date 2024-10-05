class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def makeAnagramKey(word) -> List[int]:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - 97] += 1
            return arr
        
        hm = {}

        for word in strs:
            key = tuple(makeAnagramKey(word))
            if key in hm:
                hm[key].append(word)
            else:
                hm[key] = [word]

        return hm.values()