import sys
sys.stdin = open('input.txt')

#방향 상,상우,우,하우,하,하좌,좌,상좌
dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]


for tc in range(1, int(input()) + 1):
    # 판 크기 N 및 횟수 M 입력
    N, M = map(int, input().split())
    # NxN 배열, 입력이 인덱스랑 다르므로 N+1로 생성
    arr = [[0] * (N+1) for _ in range(N+1)]
    # 기본 돌 배열
    arr[N//2][N//2] = 2
    arr[N//2][N//2 + 1] = 1
    arr[N//2 + 1][N//2] = 1
    arr[N//2 + 1][N//2 + 1] = 2
    # 횟수 M번 반복
    for _ in range(M):
        # 새로운 돌 좌표 및 돌색 입력
        i, j, color = map(int, input().split())
        # 해당 자리에 돌 놓기
        arr[i][j] = color
        # 해당 위치에서 8방향 확인
        for k in range(8):
            # 해당 방향으로 계속나가게 반복문
            l = 1
            change = []
            while l:
                # 새로운 방향
                ni = i + dir[k][0] * l
                nj = j + dir[k][1] * l
                # 중간에 낀 다른색돌 확인
                # 새방향이 범위 내라면
                if 0 <= ni <= N and 0 <= nj <= N:
                    # 만약 색이 같으면 사이의 돌 색 전부 변경
                    if arr[ni][nj] == color:
                        # 변경할 돌 길이만큼 반복
                        for z in range(len(change)):
                            arr[change[z][0]][change[z][1]] = color
                        break
                    # 끝이 만약 빈공간이면 반복문 끝
                    elif arr[ni][nj] == 0:
                        break
                    # 공 색이 다르면 바꿀 돌에 추가
                    else:
                        change.append([ni, nj])
                        l += 1
                # 범위밖으로 갔다면 끝내기
                else:
                    break
    # 검은돌 흰돌 수 세기
    bk = 0
    wh = 0
    # 전체 행렬 순회
    for m in range(N+1):
        for q in range(N+1):
            if arr[m][q] == 1:
                bk += 1
            elif arr[m][q] == 2:
                wh += 1
    print(f'#{tc} {bk} {wh}')