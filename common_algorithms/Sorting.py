# Merge sort
def mergeSort(self, arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    arr1 = self.mergeSort(arr[:mid])
    arr2 = self.mergeSort(arr[mid:])

    return self.merge(arr1, arr2)


def merge(self, left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result