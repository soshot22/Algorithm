import sys
sys.stdin = open('input.txt')
'''2진수 > 10진수 > 3진수로 변경 후 입력받은 3진수와
다른 자리수가 1개이면 출력
**기존 코드 오류 이유 한 번 쯤 보기**
'''

for tc in range(1, int(input()) + 1):
    # 입력 각 2진수 3진수
    binary = input()
    ternary = input()
    # 각 후보군을 담을 리스트
    binary_arr = []
    ternary_arr = []
    # 2진수의 길이만큼 반복
    for i in range(len(binary)):
        # 임시로 사용할 리스트
        tmp = list(binary)
        # 10진수로 반환할 값
        num = 0
        # 순회한 인덱스의 2진수 값이 1이면
        if binary[i] == '1':
            # 해당 자리의 값을 0으로 변경
            tmp[i] = '0'
            # 임시로 저장한 2진수 순회
            for j in tmp:
                if j == '1':
                    num = num * 2 + 1
                else:
                    num *= 2
            # 후보군에 추가
            binary_arr += [num]
        # 순회한 값이 0인 경우
        else:
            # 1로 변경
            tmp[i] = '1'
            # 변경 이진수 순회
            for j in tmp:
                if j == '1':
                    num = num * 2 + 1
                else:
                    num *= 2
            binary_arr += [num]
    # 10진수를 3진수로 변경
    for i in binary_arr:
        ten_num = ''
        while i:
            ten_num = str(i % 3) + ten_num
            i //= 3
        ternary_arr.append(ten_num)
    # 2진수를 변환시킨 3진수 순회
    for i in range(len(ternary_arr)):
        # 차이를 기록할 변수
        cnt = 0
        # 문자의 길이가 다를 수 있으니 더 작은 쪽의 길이 만큼만
        for j in range(min(len(ternary_arr[i]), len(ternary))):
            if ternary_arr[i][j] != ternary[j]:
                cnt += 1
        # 만약 길이가 차이 있다면 그것도 서로 다른 것이므로 추가
        cnt += abs(len(ternary_arr[i]) - len(ternary))
        # 차이가 1이면 출력
        if cnt == 1:
            print(f'#{tc} {binary_arr[i]}')
            break




