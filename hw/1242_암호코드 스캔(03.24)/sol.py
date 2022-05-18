import sys
sys.stdin = open('input.txt')
'''
1. 16진수 찾기
2. 16진수 -> 10 -> 2진수
3. 숫자판별 -> 두께 고려
4. 암호검증
'''
hex_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
    'F': '1111'}
password = {'112': '0', '122': '1', '221': '2', '114': '3', '231': '4',
            '132': '5', '411': '6', '213': '7', '312': '8', '211': '9'}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # N개의 행 생성
    arr = [[] for _ in range(N)]
    result = 0
    for i in range(N):
        val = input()
        for j in val:
             arr[i] += hex_bin[j]
    # 행 확인
    for i in range(N):
        # 열 확인
        k = len(arr[i]) - 1
        # 최소 56자리 이므로 55까지만
        while k > 54:
            # 해당 열이 1이고 바로 위의 행값이 0인 경우만
            if arr[i][k] == '1' and arr[i-1][k] == '0':
                # 패스 검증할 조합
                pass_result = ''
                # 8개의 수를 찾기 위한 반복문
                for _ in range(8):
                    # 4번째 비율
                    pass_one = 0
                    # 3번째 비율
                    pass_two = 0
                    # 2번째 비율
                    pass_three = 0
                    # 제일 끝 1이 이어지면 +1
                    while arr[i][k] == '1':
                        pass_one += 1
                        k -= 1
                    # 두번째인 0이 계속 이어지면 +1
                    while arr[i][k] == '0':
                        pass_two += 1
                        k -= 1
                    # 세 번째인 1이 계속 이어지면 +1
                    while arr[i][k] == '1':
                        pass_three += 1
                        k -= 1
                    # 마지막 비율은 계산 안할 것이니 지나감
                    while arr[i][k] == '0':
                        k -= 1
                    # 최소 비율인 값 찾기
                    min_num = min(pass_one, pass_two, pass_three)
                    # 최소 비율(1이 되는 값)으로 나누기
                    pass_one //= min_num
                    pass_two //= min_num
                    pass_three //= min_num
                    # 각 비율을 조합한 값을 패스워드(딕셔너리)에서 찾아 문자열로 합쳐줌
                    pass_result = password[str(pass_one) + str(pass_two) + str(pass_three)] + pass_result
                # 암호 검증, 마지막 검증코드로 시작
                pass_num = int(pass_result[7])
                for l in range(7):
                    # 인덱스가 홀수 이므로 짝수번째 번호
                    if l % 2:
                        pass_num += int(pass_result[l])
                    # 인덱스가 짝수이므로 홀수번째 번호
                    else:
                        pass_num += int(pass_result[l]) * 3
                # 번호를 나누었을 때 10의 배수이면
                if pass_num % 10 == 0:
                    result += sum(list(map(int, pass_result)))
            # 다음 열 탐색
            else:
                k -= 1

    print(f'#{tc} {result}')
