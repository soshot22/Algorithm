# stack 이라는 자료 구조
# 내가 정의하는 ADT(class 사용)
class Stack:
    # stack이 최초 생성 될 때 필요한 정보들
    # stack의 크기를 기본 값으로 받아야함
    def __init__(self, size,):
        # stack의 크기
        self.size = size
        # stack을 저장할 자료 구조
        # 최초 stack 생성 시 각 위치에는 값이 없다.(None)
        self.arr = [None] * size # [0, 0] 0은 0이라는 값을 가진 것
        # stack의 최상단
        self.top = -1
    # stack이 비어있는 지 확인
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    def is_full(self):
        if self.top == self.size-1:
            return True
        else:
            return False
    # stack의 추가 연산 == push, top 위치에 값을 입력
    def push(self, n):
        # 어디에?
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        self.top -= 1
        return self.arr[self.top + 1]
        
s1 = Stack(5)
print(s1.arr) # [None, None, None, None, None,]
print(s1.size) # 5
print(s1.top) # -1
s1.push('A'); s1.push('B'); s1.push('C'); s1.push('D');
s1.push('E'); print(s1.arr); print(s1_ls_full());

