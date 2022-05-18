import sys
sys.stdin = open('input.txt')
''' 좌표를 *2를 하는 경우 좌표 0.5 이동x 1씩 이동
1. 이동   2. 겹치는 좌표(삭제리스트) 3. 삭제리스트 좌표 삭제
4002 roop
'''
di, dj = [[1,-1,0,0],[0,0,-1,1]]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 좌표 *2
    result = 0
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2
    for _ in range(4002):   # 끝에서 끝까지 순회(-2000 ~ 2000)
        # 좌표이동
        for i in range(len(arr)):
            arr[i][0] += dj[arr[i][2]]
            arr[i][1] += di[arr[i][2]]
        # 중복되면 삭제후보
        ddel, v = set(), set()
        for i in range(len(arr)):
            ci, cj = arr[i][0], arr[i][1]
            if (ci, cj) in v:
                ddel.add([ci, cj])
            v.add((ci, cj))
        # 삭제 리스트에 있으면 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                result += arr[i][3]
                arr.pop(i)
        if len(arr) < 2:
            break
    print(f'#{tc} {result}')