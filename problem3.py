class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = start = 0
        dicts = {}
        for i, value in enumerate(s):
            if value in dicts and start <= dicts[value]:
                start = dicts[value] + 1 
            else:
                num = i - start + 1
                if num > maxl:
                    maxl = num
            dicts[value] = i
        return maxl