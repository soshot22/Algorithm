import sys
sys.stdin = open('input.txt')

def preorder(node):
    # 해당 노드 값이 있다면
    if node:
        print(f'{node}', end=' ')
        # 해당 노드의 왼쪽 조사
        preorder(tree[node][0])
        # 해당 노드의 오른쪽 조사
        preorder(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(f'{node}', end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(f'{node}', end=' ')


# 각 노드의 수
V = int(input())
# 간선의 수
E = V - 1
# 간선 정보
arr = list(map(int, input().split()))
# 리스트 하나에 정보 저장
tree = [[0, 0, 0] for _ in range(V+1)]
for i in range(E):
    parent, child = arr[i*2], arr[i*2 + 1]
    # 왼쪽 자식이 없다면 먼저 채움
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    # 자식 노드에 부모 값 추가
    tree[child][2] = parent
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()


