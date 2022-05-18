import sys
sys.stdin = open('input.txt')

# tc 입력받디
for tc in range(int(input())):
    # 수열의 수 N 과 작업횟수 M 입력받기
    N, M = map(int, input().split())
    # 수열입력
    numbers = list(map(int, input().split()))
    # 제일 앞의 수를 제일 뒤로 인자로 M번 반복
    for i in range(M):
        numbers.append(numbers.pop(0))
    # 제일 첫 값 추출
    result = numbers[0]

    # # 작업 횟수만큼 리스트 만들기
    # numbers += [0] * M
    # # 수열 뒤를 순서에 맞게 입력
    # for i in range(M):
    #     numbers[N+i] = numbers[i]
    # # 생성한 수열의 제일 끝과 기존 수열 수와 일치하는 인덱스 찾기
    # last_num = 0
    # for i in range(N):
    #     if numbers[-1] == numbers[i]:
    #         last_num = i
    #         break
    # # 기존 수열의 오른쪽 값(제일 앞에 있어야 하는 값)
    # result = numbers[i+1]
    print(f'#{tc+1} {result}')