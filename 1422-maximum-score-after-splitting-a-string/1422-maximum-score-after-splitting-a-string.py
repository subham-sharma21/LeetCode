class Solution:
    def maxScore(self, s: str) -> int:
        i = 1
        lCount = 0
        rCount = 0
        arr_score = []
        while i<len(s):
            left = s[:i]
            right = s[i:]
            i+=1
            lCount = left.count("0")
            rCount = right.count("1")

            score = f'{lCount} + {rCount}'
            score_sum = lCount + rCount
            arr_score.append(score_sum)
        return max(arr_score)

            

        