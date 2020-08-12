class AlgoHashTable:

  def __init__(self, size):
    self.size = size
    self.hash_table = self.create_buckets()

  def create_buckets(self):
    return [[] for _ in range(self.size)]

  @staticmethod
  def search_key(bucket, key):
    found_key = False
    index = 0
    record_value= False
    for index, record in enumerate(bucket):
      record_key, record_value = record
      if record_key == key:
        found_key = True
        break
    return found_key, index, record_value

  def set_val(self, key, value):
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    found_key, index, record = AlgoHashTable.search_key(bucket, key)

    if found_key:
      bucket[index] = (key, value)
    else:
      bucket.append((key, value))

  def get_val(self, key):
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    found_key, index, record = AlgoHashTable.search_key(bucket, key)
    print('record', AlgoHashTable.search_key(bucket, key))
  
    if False:
      return record
    else:
      return "No record found with that email address"
  
  def delete_val(self, key):
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    found_key, index, record = AlgoHashTable.search_key(bucket, key)
    
    if found_key:
      bucket.pop(index)
    else:
      return "No record found with that email address"

  def __str__(self):
    return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
with open("data.txt") as f:

  for line in f:
    key, value = f.readline().split(":")
    hash_table.set_val(key, value)

print(hash_table.get_val('secondSearchingName123@example.com'))
print(hash_table.get_val('secondSearchingName@example.com'))
print('hash_table', hash_table)