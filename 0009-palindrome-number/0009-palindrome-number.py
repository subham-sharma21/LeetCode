class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        x1 = x
        if(x<0):
            return False
        elif(x>0):    
            while (x>0):
                r = x%10
                rev = rev*10+r
                x = x//10
                 
        if (x1==rev):
            return True
        else:
            return False    