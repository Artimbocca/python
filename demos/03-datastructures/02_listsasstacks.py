stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print (stack)       # [3, 4, 5, 6, 7]

print (stack.pop()) # 7

print (stack)       # [3, 4, 5, 6]

stack.pop()         # 6

stack.pop()         # 5

print (stack)       # [3, 4]
