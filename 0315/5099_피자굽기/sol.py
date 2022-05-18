import sys
sys.stdin = open('input.txt')

# tc 입력 받기
for tc in range(int(input())):
    # 화덕의 크기 N, 피자의 수 M
    N, M = map(int, input().split())
    # 피자의 치즈 수
    cheeze = list(enumerate(map(int, input().split()), start=1))
    print(cheeze)
    # 큐생성
    queue = []
    # 화덕의 크기만큼 [피자의 치즈 수, 피자 순서] 추가
    # for i in range(N):
    #     queue.append([cheeze[i], i])
    for i in range(N):
        queue.append(cheeze[i])
    put = cheeze[N:M]
    print(put)
    # 완성한 피자의 수
    # cnt = 0
    while queue:
        # 치즈 수를 확인하기 위해 추출
        i, cheeze_i = queue.pop(0)
        # 치즈가 남았다면 치즈 수를 줄인 뒤 다시 넣기
        cheeze_i //= 2
        if cheeze_i:
            # cheeze_i //= 2
            queue.append((i, cheeze_i))
        # 치즈가 없는 경우
        else:
            # 아직 넣을 피자가 있는 경우
            if put:
                queue.append(put.pop(0))
            # # 아직 넣을 피자가 있는 경우
            # if N + cnt < M:
            #     # 피자와 인덱스 번호 넣기
            #     queue.append([cheeze[N + cnt], cnt + N])
            #     # 완성된 피자 수 +1
            #     cnt += 1
    # 인덱스 번호이므로
    result = i
    print(f'#{tc+1} {result}')