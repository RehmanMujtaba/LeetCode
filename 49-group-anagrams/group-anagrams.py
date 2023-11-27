class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for item in strs:
            counts_array = [0] * 26

            for letter in item:
                counts_array[ord("z") - ord(letter)] += 1
            
            if tuple(counts_array) in hashmap:
                hashmap[tuple(counts_array)].insert(0, item)
            else:
                hashmap[tuple(counts_array)] = [item]

        answer = []
        for key, value in hashmap.items():
            answer.insert(0, value)
            
        return answer
