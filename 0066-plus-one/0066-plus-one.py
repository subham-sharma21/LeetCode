class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int(''.join(map(str, digits)))
        x+=1
        res = list(map(int, str(x)))
        print(res)
        