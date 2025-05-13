from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to store groups of anagrams
        grouped_anagrams = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the string to get a key representing its anagram group
            sorted_str = ''.join(sorted(s))
            
            # Append the original string to the corresponding anagram group
            grouped_anagrams[sorted_str].append(s)
        
        # Return the values of the defaultdict as a list of lists
        return list(grouped_anagrams.values())
