class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Using string word find, easiest solution.
        # This string method would returns the lowest index or first occurrence of the substring if it is found in a given string.
        return haystack.find(needle)
