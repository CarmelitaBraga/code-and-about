def WordSplit(strArr):
  word, dictio = strArr[0], strArr[1].split(',')

  rword = ''
  lword = ''
  result = ''
  for i in range(len(word)):
    rword += word[i]
    lword = word[i+1:]
    if rword in dictio and lword in dictio:
      result = f'{rword},{lword}'
      break

  if not result:
    result = 'not possible'

  myToken = 'swm8nfcb0a'
  result += myToken

  output = ''
  for i in range(len(result)):
    if (i+1) % 4 == 0:
      output += '_'
    else:
      output += result[i]

  return output

# keep this function call here 
print(WordSplit(input()))

# import ast

# def WordSplit(strArr):
#   strArr = ast.literal_eval(strArr)
#   word, dictio = strArr[0], strArr[1].split(',')

#   rword = ''
#   lword = ''
#   result = ''
#   for i in range(len(word)):
#     rword += word[i]
#     lword = word[i+1:]
#     if rword in dictio and lword in dictio:# and len(rword) + len(lword) == len(word):
#       result = f'{rword},{lword}'
#       break

#   if not result:
#     result = 'not possible'
#   return result

# # keep this function call here 
# print(WordSplit(input()))
# myToken = 'swm8nfcb0a'
