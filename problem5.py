class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls=len(s)
        lmax=1
        start=end=0
        for i in range(ls):
            l=r=i 
            while True: 
                if l>=1 and r<=ls-2 and s[l-1]==s[r+1]:
                    l-=1
                    r+=1
                else: 
                    break
            if lmax<r-l+1:
                lmax=r-l+1
                start=l
                end=r
            if i<=ls-2 and s[i]==s[i+1]:
                l=i
                r=i+1
                while True: 
                    if l>=1 and r<=ls-2 and s[l-1]==s[r+1]:
                        l-=1
                        r+=1
                    else: 
                        break
                if lmax<r-l+1:
                    lmax=r-l+1
                    start=l
                    end=r
        return s[start:end+1] 