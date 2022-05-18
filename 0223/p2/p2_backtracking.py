def process_solution(arr, k, result):
    if result != 10:
        return

    for i in range(1, k+1):
        if arr[i]:
            print(data[i], end=' ')
    print()

def construct_candidator(arr, k, N, c):
    # 부분집합을 구할 것이기 때문에
    # 넣거나 안넣거나 2가지 경우의 수 밖에 없음
    c[0] = True
    c[1] = False
    return 2

# arr : 해당 원소를 사용했는지 안했는지, 원소를 직접 집어 넣을 list
# k : 현재 어디까지 조사중인지 확인할
# N : 내가 최대 조사해야 할 대상의 길이
# result
def backtracking(arr, k, N, result):
    global cnt
    # 유망성 조사를 할 리스트
    if result > 10:
        return

    c = [0] * MAXCANDIDATES

    # 현재 조사상황 == 최대 조사 상황 (재귀의 기저까지 왔다면)
    if k == N:
        # 내가 원하는 수식이 만들어 졌는지 확인할 함수
        process_solution(arr, k, result)
    else:
        k += 1
        ncandidates = construct_candidator(arr, k, N, c)
        for i in range(ncandidates):
            # 내가 집어 넣어준 arr의 k번째의 값을 쓰거나 안쓰거나
            arr[k] = c[i]
            if arr[k]:
                backtracking(arr, k, N, result + data[k])
            else:
                backtracking(arr, k, N, result)
    cnt += 1

# 유망성 조사를 위한 변수
MAXCANDIDATES = 100
NMAX = 100

cnt = 0
data = list(range(11))
arr = [0] * NMAX
backtracking(arr, 0, 10, 0)
print(cnt)