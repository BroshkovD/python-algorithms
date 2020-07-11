def merge_lists(arr1, arr2):
  sorted_arr = []
  i, j = 0, 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      sorted_arr.append(arr1[i])
      i += 1
    else:
      sorted_arr.append(arr2[j])
      j += 1
  return sorted_arr + arr1[i:] + arr2[j:]

def merge_sort(arr):
  if len(arr) < 2:
    return arr[:]
  else:
    middle = len(arr) // 2
    l1 = merge_sort(arr[:middle])
    l2 = merge_sort(arr[middle:])
    return merge_lists(l1, l2)
