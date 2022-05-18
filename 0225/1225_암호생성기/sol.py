import sys
sys.stdin = open('input.txt')

class Queue:
    def __init__(self, size):
        self.size = size
        self.item = [None] * self.size
        self.rear = 0
        self.front = 0

    def enQueue(self, el):
        self.rear = (self.rear + 1) % self.size
        self.item[self.rear] = el

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        return self.item[self.front]


def password(arr):
    a = Queue(8)
    for i in arr:
        a.enQueue(i)
    stop = 1
    while stop:
        for i in range(1, 6):
            b = a.deQueue()
            if b - i <= 0:
                a.enQueue(0)
                stop = 0
                break
            else:
                a.enQueue(b-i)
    ls = []
    for i in range(8):
        ls += [a.deQueue()]
    for i in ls:
        if i == 0:
            ls = ls[i:]+ls[:i]
    return ls

for tc in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    result = password(arr)
    print(f'#{tc}', end= '')
    for i in range(8):
        print(f' {result[i]}', end='')
    print()

