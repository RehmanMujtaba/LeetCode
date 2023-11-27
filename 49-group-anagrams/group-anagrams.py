class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for item in strs:
            counts_array = [0] * 26

            for letter in item:
                counts_array[ord("z") - ord(letter)] += 1
            
            hashmap[tuple(counts_array)].append(item)

        return hashmap.values()