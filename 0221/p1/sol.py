def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]

size = 3
stack=[0]*size
top = -1
push(1, size)
print(stack)
push(2, size)
print(stack)
push(3, size)
print(stack)
print(pop())
print(pop())
print(pop())