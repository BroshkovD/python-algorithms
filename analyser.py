import time
import random
from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from inserting_sort import inserting_sort

def random_list_generator(size, max_value):
  result = []

  for i in range(size):
    result.append(random.randint(1, max_value))
  
  return result

def analyze_func(func_name, arr):
  tic = time.time()
  func_name(arr)
  toc = time.time()
  seconds = toc-tic
  print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
run_times = int(input("How many times do you want to run? "))

for num in range(run_times):
  print(f"Run: {num+1}")
  l = random_list_generator(size, max)
  analyze_func(quick_sort, l)
  analyze_func(merge_sort, l)
  analyze_func(bubble_sort, l.copy())
  analyze_func(inserting_sort, l.copy())
  analyze_func(sorted, l)
  print("-" * 40)