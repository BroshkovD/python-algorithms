def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[-1]
    smaller, equal, larger = [], [], []
    for num in arr:
      if num < pivot:
        smaller.append(num)
      elif num == pivot:
        equal.append(num)
      else:
        larger.append(num)
  return quick_sort(smaller) + equal + quick_sort(larger)