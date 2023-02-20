from typing import List, Any


def findDifference(nums1:List[int], nums2:List[int])-> List[List[int]]:
    result = [[], []]

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] not in nums2 and nums1[i] not in result[0]:
                result[0].append(nums1[i])
            if nums2[j] not in nums1 and nums2[j] not in result[1]:
                result[1].append(nums2[j])
    return result


print(findDifference([1,2,3,3], [1,1, 2, 2]))
