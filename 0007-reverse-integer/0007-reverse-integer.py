class Solution:
    def reverse(self, x: int) -> int:
        
        int_max = 2**31-1
        int_min = -2**31

        rev = int(str(abs(x))[::-1])  # Reverse the absolute value and convert back to integer
        if x < 0:
            rev = -rev  # Reapply the negative sign if the original number was negative



        if rev > int_max or rev < int_main:
            return 0
        return rev