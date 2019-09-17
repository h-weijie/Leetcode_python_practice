class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r = []
        i = j = 0
        l1 = len(nums1)
        l2 = len(nums2)
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1
        if i < l1:
            while i < l1:
                r.append(nums1[i])
                i += 1
        else:
            while j < l2:
                r.append(nums2[j])
                j += 1
        l = len(r)
        m = l // 2 
        if l % 2:
            return r[m]          
        else:
            return (r[m - 1] + r[m])/2