def find_intersection(array1, array2):
    intersection = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                if array1[i] and array2[j] not in intersection:
                    intersection.append(array1[i])
    return intersection


print(find_intersection([4, 9, 5], [9, 4, 9, 8, 4]))
