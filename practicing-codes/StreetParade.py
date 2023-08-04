from collections import deque

def reordable(queue, actual, popped, peek):
    if popped != None:
        if 
    else:
        if actual < peek:
            return False
    if len(queue) > 1:
        reordable(queue, queue.pop(), actual, s[0])
    else:
        return True


input_ = input().split()
s = deque()
for _ in input_:
    s.appendleft(int(_))

reordable = True
if len(s) > 1:
    reordable = reordable(s, s.pop(), None, s[0])
if reordable:
    print('yes')
else:
    print('no')





print(s)

s.popleft()

print(s[0])
