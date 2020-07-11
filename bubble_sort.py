def bubble_sort(l):
  swap_happened = True

  while swap_happened:
    swap_happened = False

    for item in range(len(l)-1):
      if l[item] > l[item+1]:
        l[item+1], l[item] = l[item], l[item+1]
        swap_happened = True




