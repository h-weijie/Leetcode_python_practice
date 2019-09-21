class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        elif num<=0:
            return False
        else:
            Flag = True
            while num>1:
                if num%2==0:
                    num//=2
                elif num%3==0:
                    num//=3
                elif num%5==0:
                    num//=5
                else:
                    Flag=False
                    break
            return Flag