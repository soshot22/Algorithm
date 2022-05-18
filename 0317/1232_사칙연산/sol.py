import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 정점의 수
    N = int(input())
    # 정점의 수 + 1 만큼 트리
    # [부모 노드, 값, 왼쪽 자식값, 오른쪽 자식값]
    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    # 정점의 수 만큼 순회
    for i in range(1, N+1):
        # 정점 입력 정보 리스트
        # [노드번호, 값, 왼쪽자식, 오른쪽 자식]
        info = list(input().split())
        # 정점이 기호라면
        if len(info) == 4:
            # [노드 값, 왼쪽 자식, 오른쪽 자식] 순회
            for j in range(1, 4):
                # 해당 노드 값 저장
                if j == 1:
                    tree[i][1] = info[j]
                # 해당 부모 노드 저장
                else:
                    tree[int(info[j])][0] = i
        # 리프 노드라면
        else:
            tree[i][1] = float(info[1])
    print(tree)
    k = N
    while k > 0:
        # 노드의 값이 숫자일때
        if type(tree[k][1]) == float:
            # 홀수일때(우측 자식)
            # tree[k][0] 부모 노드번호
            if k % 2:
                tree[tree[k][0]][3] = tree[k][1]
            # 짝수일때(좌측 자식)
            else:
                tree[tree[k][0]][2] = tree[k][1]
            k -= 1
        # 노드의 값이 기호일때
        else:
            if tree[k][1] == '+':
                tree[k][1] = tree[k][2] + tree[k][3]
            elif tree[k][1] == '-':
                tree[k][1] = tree[k][2] - tree[k][3]
            elif tree[k][1] == '*':
                tree[k][1] = tree[k][2] * tree[k][3]
            else:
                tree[k][1] = tree[k][2] / tree[k][3]
    tree[1][1] = int(tree[1][1] - tree[1][1] % 1)
    print(f'#{tc} {tree[1][1]}')
