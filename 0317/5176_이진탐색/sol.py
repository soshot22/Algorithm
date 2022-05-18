import sys
sys.stdin = open('input.txt')

# 중위순회 함수
def inorder(v):
    global cnt
    if v:
        inorder(tree[v][1])
        # 중간에 값 입력 후 값 증가
        tree[v][0] = cnt
        cnt += 1
        inorder(tree[v][2])

for tc in range(1, int(input()) + 1):
    # 정점의 수 입력
    N = int(input())
    # [값, 왼쪽자식, 오른쪽 자식]
    tree = [[0, 0, 0] for _ in range(N+1)]
    # 각 자식값 입력을 위한 반복문
    for i in range(1, N+1):
        # 우측 자식 값이 존재한다면
        if i*2 + 1 <= N:
            # 우측 자식 좌측 자식 입력
            tree[i][1] = i*2
            tree[i][2] = i*2 + 1
        # 좌측 자식 값이 존재한다면
        elif i*2 <= N:
            # 좌측 자식 값 입력
            tree[i][1] = i*2
    # 입력에 활용할 값 cnt
    cnt = 1
    # 중위순회 함수
    inorder(1)
    print(f'#{tc} {tree[1][0]} {tree[N//2][0]}')

