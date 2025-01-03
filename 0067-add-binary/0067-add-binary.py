class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1 = int(a, 2)
        decimal2 = int(b, 2)
        add = decimal1+decimal2
        # x = str(bin(add))
        # return x[2:]
        return str(bin(add[2:]))

        