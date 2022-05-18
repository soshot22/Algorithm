'''
[입력] TC 수/ {전체 쪽수} {A가 찾을 쪽} {B가 찾을 쪽}
[출력] #{TC} {이긴 사람 or 0}
[조건] 1. 주어진 페이지 내 찾을 쪽을 이진검색으로 찾기
2. 검색 실행 후 새 기준점은 검색한 중간쪽
'''
# input 불러오기
import sys
sys.stdin = open('input.txt')
# 총 반복횟수 TC 입력
for tc in range(int(input())):
    # 총 페이지 입력, 찾을 페이지
    P, Pa, Pb = map(int, input().split())
    # 처음 시작 페이지 1, 처음 끝 페이지 P
    start = 1
    end = P
    # a,b 의 검색 수와 중간 값 0
    cnt_a = cnt_b = middle = 0
    # 끝페이지가 시작 페이지보다 클 경우 반복
    while start <= end:
        # 중간 값 입력 및 횟수 증가
        middle = (start + end)//2
        cnt_a += 1
        # 중간값의 위치에 따라 시작 or 끝 페이지 바꿈
        if middle == Pa:
            break
        elif middle > Pa:
            end = middle
        elif middle < Pa:
            start = middle
    # 검색에 활용할 값들 초기화
    middle = 0
    start = 1
    end = P
    # 위의 방식과 동일
    while start <= end:
        middle = (start + end) // 2
        cnt_b += 1
        if middle == Pb:
            break
        elif middle > Pb:
            end = middle
        elif middle < Pb:
            start = middle
    # a,b의 검색 횟수 비교후 적은 쪽 출력
    if cnt_a < cnt_b:
        print(f'#{tc+1} A')
    elif cnt_a > cnt_b:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc + 1} 0')

