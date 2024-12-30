class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        if target in nums:
            x = nums.index(target)
            return x
        else:
            
            while pos < len(nums) and nums[pos] < target:
                pos += 1
            nums.insert(pos, target)
        return pos       