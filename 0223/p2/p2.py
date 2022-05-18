arr = list(range(1, 11))
print(arr)
N = len(arr)

def powerset(arr, idx, total):
    global count
    # 가지치기
    if sum(total) > 10:
        return
    count += 1
    # 언제까지 재귀로 순회할 것이냐
    # 내가 가지고 있는 모든 원소를 조사 했을때
    if idx == N:
        # 그 중에, 총 합이 10이 된순간
        if sum(total) == 10:
            print(total)
        return
    # arr, 다음 조사 대상, 현재 조사대상을 total에 넣거나
    powerset(arr, idx + 1, total + [arr[idx]])
    # 안 넣거나
    powerset(arr, idx + 1, total)

count = 0
powerset(arr, 0, [])
print(count)