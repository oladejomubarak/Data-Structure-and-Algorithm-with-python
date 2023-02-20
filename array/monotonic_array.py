from typing import List


def is_monotonic(nums: List[int]) -> bool:
    result = []
    for i in range(len(nums)):
        # j = i + 1
        for j in range(len(nums)):
            if nums[i] >= nums[j] or nums[i] <= nums[j]:
                result.append(True)
            else:
                result.append(False)
    for k in range(len(result)):
        if result[k]:
            print(True)
        else:
            print(False)


is_monotonic([1,2,2,3])
