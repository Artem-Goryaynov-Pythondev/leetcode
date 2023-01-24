def findMedianSortedArrays(nums1,nums2):
    commonList = nums1 + nums2
    commonList.sort()
    if len(commonList) % 2 != 0:
        a = commonList[(len(commonList) // 2)]
        return float(a)
    else:
        a = commonList[(len(commonList) // 2)]
        b = commonList[(len(commonList) // 2) - 1]
        c = (a+b)/2
        return float(c)




assert findMedianSortedArrays([1,3],[2]) == 2.00000
assert findMedianSortedArrays([1,3],[2,4]) == 2.50000

