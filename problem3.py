class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s):
            maxl = 1
        else:
            maxl = 0
        i = 0
        ls = list(s)
        for j in range(1,len(ls)):
            while s[j] in ls[i:j]:
                i += 1
            if maxl < j - i + 1:
                maxl = j - i + 1
        return maxl