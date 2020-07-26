def selection_sort(l):
  interator = 0
  lenght = len(l)

  while interator < lenght:
    for item in range(interator, lenght):
      
      if l[item] < l[interator]:
        l[interator], l[item]  = l[item], l[interator]

    interator += 1