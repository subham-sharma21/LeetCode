class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        # nums1 = num
        # nums = list(filter(lambda x: x!=0,num))
        # print(num)
        # for i in range(n):
        #     nums1.append(nums2[i])
        # nums1.sort()

        nums1.extend(nums2)
        nums1.sort()
        

        


        