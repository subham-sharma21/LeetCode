class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>9:
            s=0
            while num!=0:
                r = num%10
                num = num//10
                s=s+r
            num=s
        return num        
