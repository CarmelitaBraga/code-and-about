def SimpleMode(arr):
  dictio = {k: 0 for k in arr}

  for element in arr:
    dictio[element] += 1

  mode = -1
  bigger = next(iter(dictio))
  for k in dictio.keys():
    if dictio[k] > 1 and dictio[k] > dictio[bigger]:
      bigger = k

  # code goes here
  return mode if dictio[bigger] == 1 else bigger

# keep this function call here 
print(SimpleMode(input()))