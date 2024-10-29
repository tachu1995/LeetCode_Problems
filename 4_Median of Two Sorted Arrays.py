class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum = 0
        for i in nums2:
            nums1.append(i)
        nums1 = sorted(nums1)
        lenth = len(nums1)
        if lenth % 2==0:
            medium = (nums1[int(lenth/2)]+nums1[int(lenth/2)-1])/2
        else:
            medium = nums1[int(lenth/2)]
        return medium
        
        
