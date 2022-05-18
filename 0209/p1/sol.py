'''
각 상자의 낙차 값은 상자가 있는 곳에서 빈 줄 수가 가장
큰값
[입력값] 총 반복 횟수, 방 가로길이, 강 줄별로 쌓은 박스 수
[출력값] #{횟수} {최대 낙차값}
'''
import sys
sys.stdin = open('input.txt')

# 입력받은 값 만큼 낙차값 구하기 반복문
N = int(input())
for i in range(1, N + 1):
    # 다시 입력받은 방의 크기 변수
    room = int(input())
    # 방의 크기만큼 반복문
    # 입력 받은 박스 높이를 리스트로 만듬
    box = list(map(int, input().split()))
    gravity = 0
    for j in range(room):
        # 떨어질 높이 측정할 변수
        height = 0
        # 입력 받은 박스 높이를 리스트로 만듬
        # 박스의 우측공간 비교를 위한 반복문
        for k in range(j + 1, room):
            # j번 박스가 비교할 k번 박스 높이보다 크면 높이+1
            if box[j] > box[k]:
                height += 1
        # 기존 높이 받던 값보다 더 높으면 중력 변경
        if gravity < height:
            gravity = height
    print(f'#{i} {gravity}')

