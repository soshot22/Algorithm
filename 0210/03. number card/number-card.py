'''
[입력] 테스트 케이스 수 / 카드 장수 / 카드 수
[출력] #{케이스번호} {가장많은 카드 숫자} {장수}
[조건] 0~9 숫자 카드, 1. 가장 많은 카드에 적힌 수와 그 장수
2. 가장 많은 수의 카드가 동률 시  더 높은 숫자의 카드를 출력
'''
# input.txt 불러오기
import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수 불러오기
T = int(input())
# 총 반복 횟수 테스트 케이스의 수 만큼 반복
for i in range(T):
    # 카드장수 N
    N = int(input())
    # 카드값 입력(순회가능한 문자열로 받음)
    card = input()
    # 카드 수를 기록할 배열 생성
    arr = [0]*10
    # 문자열 card를 순회하면서 해당 숫자 배열 정리
    for j in card:
        arr[int(j)] += 1
    # 가장 많은 카드의 번호를 저장할 변수
    max_card_num = 0
    # 카드 번호의 숫자인 10번 반복
    for k in range(10):
        # 해당 번호의 숫자 비교후 같거나 높으면 최고값 카드 번호 변경
        if arr[k] >= arr[max_card_num]:
            # 결국 빈도가 높거나 같아도 더 뒤의 카드번호 저장
            max_card_num = k
    print(f'#{i + 1} {max_card_num} {arr[max_card_num]}')

