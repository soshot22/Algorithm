import sys
sys.stdin = open('input.txt')

# 전위 순회 함수
def preorder(v):
    if v:
        print(f' {v}', end='')
        preorder(arr[v][0])
        preorder(arr[v][1])       

# 중위 순회 함수
def inorder(v):
    if v:
        inorder(arr[v][0])
        print(f' {v}', end='')
        inorder(arr[v][1])
        
# 후위 순회 함수
def postorder(v):
    if v:
        postorder(arr[v][0])
        postorder(arr[v][1])
        print(f' {v}', end='')

V, E = map(int, input().split())
# 왼쪽 자식, 오른쪽 자식
arr = [[0, 0] for _ in range(V+1)]
node = list(map(int, input().split()))
for i in range(E):
    p, c = node[i*2], node[i*2 + 1]
    if arr[p][0]:
        arr[p][1] = c
    else:
        arr[p][0] = c
print('전위 순회 :', end='')
preorder(1)
print()
print('중위 순회 :', end='')
inorder(1)
print()
print('후위 순회 :', end='')
postorder(1)

