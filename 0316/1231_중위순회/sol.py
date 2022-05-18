import sys
sys.stdin = open('input.txt')

def inorder(v):
    if v:
        inorder(tree[v][1])
        # 해당 값 출력
        print(tree[v][0], end='')
        inorder(tree[v][2])

for tc in range(1, 11):
    # N은 정점의 수
    N = int(input())
    # 각 값 , 왼쪽자식, 오른쪽 자식 저장할 트리
    tree = [[0, 0, 0] for i in range((N+1))]
    # 자료가 순서대로 정점 주어지므로
    for i in range(1, N+1):
        # 각 입력을 리스트로 저장
        info = list(input().split())
        # 제일 첫 노드번호는 생각하지 않으므로 1부터
        for j in range(1, len(info)):
            # 노드 값을 트리의 첫값(인덱스는 0)에 저장
            if j == 1:
                tree[i][j - 1] = info[j]
            # 왼쪽 자식 오른쪽 자식을 정수로 변환하여 트리에 저장
            else:
                tree[i][j - 1] = int(info[j])
    # 형식을 맞추기 위해 출력
    print(f'#{tc} ', end=' ')
    # 중위 순회 형식의 함수에 입력
    inorder(1)
    print()







