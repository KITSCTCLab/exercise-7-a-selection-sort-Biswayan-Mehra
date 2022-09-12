from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
    min_index = i
    for j in range(i+1, size):
      if array[min_index]>array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
      

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
