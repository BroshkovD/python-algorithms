def inserting_sort(l):

  for item in range(1, len(l)):
    if l[item] < l[item-1]:      
      index = item
      while index >= 1 and l[index] < l[index-1]:
        l[index-1], l[index] = l[index], l[index-1]
        index -= 1