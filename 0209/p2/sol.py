import sys
sys.stdin = open('input.txt')
# 활용 함수 생성 인자는 반복 횟수 N과 6자리수(문자형)
def baby_gin(number):
    count = [0] * 10
    triplet = 0
    run = 0
    for j in range(6):
        count[(number % 10) - 1] += 1
        number = number // 10
        k = 0
        while k < 10:
            if count[k-1] >= 1 and count[k] >= 1 and count[k+1] >= 1:
                run += 1
                count[k-1] -= 1
                count[k] -= 1
                count[k+1] -=1
                continue
            if count[k] >= 3:
                triplet += 1
                count[k] -= 3
                continue
            k += 1
    if run + triplet > 1:
        return 1
    else:
        return 0
for i in range(1, int(input()) + 1):
    result = baby_gin(int(input()))
    print(f'#{i} {result}')





