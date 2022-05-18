import sys
sys.stdin = open('input.txt')

# 최소힙 구현
for tc in range(1, int(input()) + 1):
    # 정점 값 입력
    N = int(input())
    # 힙을 구성할 수들 입력
    arr = list(map(int, input().split()))
    last = 1
    # 트리 생성
    tree = [0] * (N+1)
    for i in range(N):
        # 루트에 값(시작) 넣기
        if tree[last] == 0:
            tree[last] = arr[i]
        # 비교
        else:
            # 기존 값 +1
            last += 1
            # 자식값
            c = last
            # 부모값
            p = c // 2
            # 이전 입력값 다음 값에 값 넣기
            tree[c] = arr[i]
            # 부모값이 자식값 보다 크다면 계속 교체
            while tree[p] > tree[c]:
                tree[p], tree[c] = tree[c], tree[p]
                # 다시 기존 부모값은 자식값으로
                c = p
                # 부모값은 기존 부모값의 부모값으로 교체
                p = p//2
    # 결과 저장 값
    result = 0
    # 조상노드가 있을 때(1)까지 반복
    while N//2:
        result += tree[N//2]
        N //= 2
    print(f'#{tc} {result}')



