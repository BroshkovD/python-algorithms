from random import choice
from string import ascii_letters
from time import time
from bisection_iter import bisection_iter

print(bisection_iter)
##### functions to generate lists of random emails ####
def generate_name(length_of_name):
  return ''.join(choice(ascii_letters) for i in range(length_of_name))

def get_domain(list_of_name):
  return choice(list_of_name)

def generate_emails(length_of_name, list_of_domains, total_emails):
  emails = []
  for num in range(total_emails):
    emails.append(generate_name(length_of_name)+"@"+get_domain(list_of_domains))
  return emails

def analyze_func(func_name, *args):
  tic = time()
  func_name(*args)
  toc = time()
  seconds = toc - tic
  print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds: .5f}")


# Generate emails
list_of_domains = ['yaxample.com', 'goexample.com', 'example.com']
emails = generate_emails(10, list_of_domains, 1000) 

# Test email to add to list of emails
email = "find.this.email@example.com"
emails.append(email)

# Sort list of generated email
sorted_emails = sorted(emails)

# Run bisection search to find test email
index, found = bisection_iter(email, sorted_emails)

# Print result from function
print(found)

# Print index returned by function
if index: print(f"Element at index: {index} is {sorted_emails[index]}")

# Run analysis of functions
analyze_func(bisection_iter, email, sorted_emails)
analyze_func(generate_emails, 10, list_of_domains, 100000)