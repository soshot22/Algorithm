import sys
sys.stdin = open('input.txt')

def preorder(v):
    # 전위 순회 함수
    global result
    # 해당 자식 값이 있다면 0이 아니므로
    if v:
        # 해당 노드값을 더함 
        result += 1
        # 좌측 자식 값을 입력
        preorder(tree[v][0])
        # 우측 자식 값을 입력
        preorder(tree[v][1])


for tc in range(1, int(input()) + 1):
    # E와 노드번호 N 입력
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 노드 번호는 1~ E+1 이므로 트리는 E+2까지 생성
    tree = [[0, 0]for _ in range(E+2)]
    # 간선 표시를 위한 반복문
    for i in range(E):
        # 왼쪽 자식노드가 비었다면 해당 자식 노드 입력
        if tree[arr[i*2]][0] == 0:
            tree[arr[i*2]][0] = arr[i*2 + 1]
        # 오른쪽 자식 노드가 비었다면 입력
        else:
            tree[arr[i*2]][1] = arr[i*2 + 1]
    result = 0
    # 결과값을 찾을 함수에 입력
    preorder(N)
    print(f'#{tc} {result}')

