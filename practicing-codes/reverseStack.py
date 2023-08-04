from collections import deque

def reverse(stack, i):
    if i > 0:
        addReversed(stack, None, stack.pop(), i)
        i -= 1
        reverse(stack, i)


def addReversed(stack, top, element, i):
    if i == 0:
        stack.append(element)
    else:
        i -= 1
        addReversed(stack, stack.pop(), element, i)
    if top != None: stack.append(top)


s = deque("abcd")
print(s)
reverse(s, len(s)-1)
print(s)
