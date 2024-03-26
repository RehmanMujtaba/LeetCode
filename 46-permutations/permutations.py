from math import factorial
class Solution:  
    def permute(self, nums: List[int]) -> List[List[int]]:
        def nth_permutation(n, nums):
            permutation = []
            factoradic = []
            
            # Calculate factoradic representation
            for i in range(1, len(nums) + 1):
                factoradic.append(n % i)
                n //= i
            factoradic.reverse()
            
            # Generate permutation based on factoradic representation
            for i, f in enumerate(factoradic):
                permutation.append(nums.pop(f))
            return permutation
        
        num_permutations = factorial(len(nums))
        permutations = []
        
        # Generate all permutations
        for i in range(num_permutations):
            permutations.append(nth_permutation(i, nums[:]))
        
        return permutations