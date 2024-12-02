#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
      def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Count the occurrences of each character in both strings
        char_count_s = {}
        char_count_t = {}

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Compare the character counts
        return char_count_s == char_count_t
        
        
# @lc code=end
