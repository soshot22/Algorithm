import sys
sys.stdin = open('input.txt')

def baby(ls):
    global result
    # 버블 정렬로 오름차순 정렬
    for i in range(3):
        for j in range(i, 0, -1):
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
    # a = b 이고 b = c이면 a = c 이므로 triplet
    if ls[0] == ls[1] and ls[1] == ls[2]:
        result = 1
        return
    # run
    if ls[0] + 1 == ls[1] and ls[1] + 1 == ls[2]:
        result = 1
        return

# (배열, 뽑을 수, 현재 진행 위치, 뽑은 배열)
def Comb(arr, r, k, ls):
    # 전체 배열의 길이
    N = len(arr)
    # 뽑을 수가 더 이상 없다면
    if r == 0:
        baby(ls)
        return
    # 해당 순회는 현재 위치 ~ 전체 길이 - 뽑을 수까지 순회
    # 3C3의 경우(N=3, r=3) (0 , 3-3 +1 = 1) : 0번 선택
    # (1, 3-2 +1 = 2): 1번 선택, (2, 3-1 +1 = 3): 2번 선택
    for i in range(k, N-r+1):
        Comb(arr, r-1, i+1, ls+[arr[i]])

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    # 각자가 받을 리스트
    a_arr = list()
    b_arr = list()
    result = 0
    # 12번 반복
    for i in range(12):
        # 인덱스가 홀수(짝수번째 차례)이므로 b에 추가
        if i % 2:
            b_arr.append(arr[i])
            # 1, 3, 5부터 3개 이상 이므로
            if i >= 5:
                # 조합 생성에 넣고
                Comb(b_arr, 3, 0, [])
                # 결과가 나왔다면 플레이어 2의 승이므로 2로 변경
                if result:
                    result = 2
                    break
        # 인덱스가 짝수번째(배열의 홀수 번)
        else:
            a_arr.append(arr[i])
            # 0, 2, 4부터 3개
            if i >= 4:
                Comb(a_arr, 3, 0, [])
                # 베이비진의 뭐든 걸리면
                if result:
                    break
    print(f'#{tc} {result}')