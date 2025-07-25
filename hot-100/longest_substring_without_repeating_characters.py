# Time Complexity: O(n)
# - Each character is visited at most twice (once by right, once by left).
#
# Space Complexity: O(min(n, k))
# - n is the length of the input string.
# - k is the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).
# Idea:
# Use the sliding window technique with a hash map to keep track of the most recent index
# of each character in the string. As we iterate through the string with a right pointer,
# we check if the current character has already appeared within the current window.
# If it has, we move the left pointer to one position after the previous occurrence
# of the repeated character. This ensures the substring between left and right contains
# only unique characters.


class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        char_index_map={}
        left=0
        maxLength=0
        
        for right in range (len(s)):
            char=s[right]
            if char in char_index_map and char_index_map[char]>=left:
                left=char_index_map[char]+1 
                
            char_index_map[char]=right
            maxLength=max(maxLength,right-left+1)
            
        return maxLength
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(sol.lengthOfLongestSubstring("abba"))      # Output: 2



    
        