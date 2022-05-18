import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    # 노드 수(N), 리프 노드 수 (M), 출력 노드(L)입력
    N, M, L = map(int, input().split())
    # 트리는 노드수 +1
    tree = [0] * (N+1)
    for i in range(M):
        # 리프 노드 번호(n) 그 값(v) 입력
        n, v = map(int, input().split())
        tree[n] = v
    # 마직막 리프 노드는 N이 끝값이므로
    k = N
    # 전체 노드를 N부터 2까지 순회할 함수
    while k > 1:
        # 각 값을 부모 노드에 더해줌 리프 노드의 값들이 있으므로 그 바로 윗 레벨은 채워짐
        tree[k//2] += tree[k]
        k -= 1
    # L까지 구하는 경우
    # while k > L:
    #     tree[k//2] += tree[k]
    #     k -= 1
    print(f'#{tc} {tree[L]}')