import sys
sys.stdin = open('input.txt')
# [i, j, cnt, dir] 좌표 기억 내용
# 방향 [] 반대 방향 [] 배열을 만들면 오히려 편함
di, dj = (0, -1, 1, 0, 0), (0, 0, 0, -1, 1)
opp = [0, 2, 1, 4, 3] # 1일 땐 2 2일땐 1 3일땐 4 4일땐 3 방향
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 총 반복 횟수
    for _ in range(M):
        # [1] 각각의 미생물 이동, 경계처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 경계 처리
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2     # 반 죽이기
                arr[i][3] = opp[arr[i][3]]  # 반대 방향으로 변경
        # [2] 좌표, 개수에 따른 내림차순 정렬 실행(중복 위치 확인)
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        # [3] 같은 좌표인 경우, 큰 미생물로 합치기
        i = 1   # 1부터 시작하게 N+1개 만들었으므로
        while i < len(arr):
            # 동일 좌표라면
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] ==arr[i][1]:
                arr[i-1][2] += arr[i][2] # 미생물 합치기
                arr.pop(i) # 합쳐진 좌표 없애기 다시 확인해야하므로 i 변화 x
            else:
                i += 1
    ans = 0
    # 총 미생물 수 구하기
    for i in range(len(arr)):
        ans += arr[i][2]
    print(f'#{tc} {ans}')