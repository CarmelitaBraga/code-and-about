nums = input().split()

res = [] #set()
n = len(nums)
for i in range(n):
    res.append(nums[i])
    cum = []
    j = i + 1
    while j < len(res):
        
        cum.append(nums[j])
        res.append(cum)
    
print(res)
