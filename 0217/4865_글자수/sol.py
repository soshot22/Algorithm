import sys
sys.stdin = open('input.txt')

def func(str_1, str_2):
    # 빈 딕셔너리
    new_dic = {}
    # 첫 문자열을 순회하며 키값 생성(키는 유일값)
    for i in str_1:
        new_dic[i] = 1
    # 최대값 변수 겸 초기화 위치
    max_cnt = 0
    # 딕셔너리의 키값(알파벳)만 순회
    for j in new_dic:
        # 해당 알파벳 카운트 변수
        cnt = 0
        # 두번째 문자 값 순회
        for k in str_2:
            # 첫번째 문자 글자가 두번째 문자에 있는 경우 +1
            if j == k:
                cnt += 1
        # 해당 문자 수가 최댓값보다 큰 경우 최댓값 교체
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt

# 입력값들 불러오기
for tc in range(int(input())):
    a = input()
    b = input()
    # 입력값들 함수에 넣은 후 출력 형식에 맞춰 출력
    c = func(a, b)
    print(f'#{tc+1} {c}')



