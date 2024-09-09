def CoinDeterminer(num):
  cs = [1,5,7,9,11]

  distance = num
  numCoins = 0

  for i in range(len(cs)-1, -1, -1):
    if distance >= cs[i]:
      numCoins += distance // cs[i]
      distance -= numCoins * cs[i]
    if distance == 0:
      break

  # code goes here
  return numCoins

# keep this function call here 
print(CoinDeterminer(input()))