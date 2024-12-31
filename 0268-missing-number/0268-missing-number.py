class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of array
        sum = 0
        for i in nums:
            sum = sum + i

        #sum of n natural number
        n = len(nums)
        nsum = int((n*(n+1))/2)

        ans = nsum - sum
        return ans

            
              

        