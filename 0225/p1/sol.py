# 큐 클래스 생성
class Queue:
    # 큐 생성
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = -1
        self.front = -1
    # 인큐 함수
    def enQueue(self, el):
        if self.isFull():
            print('Queue is Full')
        else:
            self.rear += 1
            self.items[self.rear] = el
    # 디큐 함수
    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            self.front += 1
            return self.items[self.front]
    # 큐의 칸 확인
    def isEmpty(self):
        return self.front == self.rear
    # 큐가 찼는지 확인
    def isFull(self):
        return self.rear == self.size -1
    # 큐의 제일 마지막 값 반환
    def Qpeek(self):
        return self.items[self.front]

q = Queue(3)
q.enQueue(1)
print(q.items)
q.enQueue(2)
print(q.items)
q.enQueue(3)
print(q.items)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.items)


            
    


    