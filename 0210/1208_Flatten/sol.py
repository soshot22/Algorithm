'''
[입력] 덤프횟수 / 상자높이
[출력] #{테스트 케이스 번호} {최저점과 최고점 높이차}
[조건] 1. 덤프 : 가장 높은 곳의 상자 하나를 가장 낮은 곳에 옮기는 작업
2. 덤프 횟수 제한
3. 평탄화 작업을 모두 수행 시  높이차는 0 or 1
4. 가로길이(박스를 나둬야하는 곳 100 테스트 케이스 10 고정값
[작업] 1. 오름차순으로 정렬 2. 덤프 작업(가장 우측 -1 가장 좌측 +1)
3. 변경 값들의 각각 바로 우측과 좌측값과 비교 후 필요시 교체
4. 평탄화의 끝은 횟수 n을 채우거나 땅 높이 최대차가 1 or 0(둘은 동시에 옮)
'''
# input.txt 불러오기
import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수는 10으로 주어졌으니 10번 반복
for tc in range(10):
    # 입력값 변수로 만듬
    n = int(input())
    box_height = list(map(int, input().split()))
    # 박스 높이에 따라 오름차순 정렬
    for i in range(99, 0, -1):
        for j in range(0, i):
            if box_height[j] > box_height[j+1]:
                box_height[j], box_height[j+1] = box_height[j+1], box_height[j]
    # 정렬한 리스트를 덤프 횟수 n번 시행
    for k in range(n):
        # 정렬한 최댓값과 최솟값이 1이하이면 종료
        if box_height[-1] - box_height[0] <= 1:
            break
        # 가장 큰 값은 -1 가장 작은 값은 +1
        box_height[-1] -= 1
        box_height[0] += 1
        # 바로 옆 값들과 비교
        min_k = 0
        # 덤프된 최솟값이 바로 우측 값들보다 크다면 우측으로 이동
        while box_height[min_k] > box_height[min_k + 1]:
            box_height[min_k], box_height[min_k + 1] = box_height[min_k + 1], box_height[min_k]
            min_k += 1
        max_k = -1
        # 덤프된 최댓값이 바로 좌측 값들보다 작다면 좌측 이동
        while box_height[max_k] < box_height[max_k -1]:
            box_height[max_k], box_height[max_k -1] = box_height[max_k -1], box_height[max_k]
            max_k -= 1
    # 형식에 맞춰 출력
    print(f'#{tc + 1} {box_height[-1] - box_height[0]}')