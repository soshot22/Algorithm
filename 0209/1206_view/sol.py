'''
가로 세로 최대 1000 x 255으로 주어진다.
양쪽 2칸에 나와 같은 높이인 빌딩x 면 조망권
시작 끝 바로 2칸에는 건물x
[입력] 총 10개의 테스트 케이스 케이스 케이스 길이 + 빌딩높이
[출력] #1 691 형태
[문제 해결 방법] 1. 각 빌딩의 높이를 토대로 순회 필요
2. 순회 비교대상 (좌우 2칸 빌딩 높이 4개 중 가장 높은 빌딩)
2-1 비교방식 1개씩 비교(높이 차가 제일 적은 값 추출도 필요)
2-2 비교대상 간 비교 후 가장 높은 빌딩과 비교
3. 조망권 확보층 마다 값을 더해야함 
'''
import sys
sys.stdin = open('input.txt')
# 생성 함수, 입력 받은 길이와 각 빌딩 높이를 입력
def vil(N, floor):
    # 최종 결과 저장 변수
    green = 0
    # 처음과 마지막 2칸은 건물이 없으니 순회 X
    for i in range(2, N - 2):
        # 양쪽 2개 빌딩 중 가장 큰 값 찾을 때 사용할 변수
        height = 0
        for j in range(-2, 3):
            # 자기 자신은 제외하고 인접 빌딩 중 가장 큰 값 찾기
            if i + j != i and floor[i + j] > height:
                height = floor[i + j]
        # 근처 가장 큰 빌딩과 자기 자신 비교
        if floor[i] > height:
            green += (floor[i] - height)
    return green
# 입력 값 적용을 위해 주어진 테스트케이스 10회 만큼 반복
for _ in range(1, 11):
    # 작성한 함수에 맞게 각 값들 입력
    result = vil(int(input()), list(map(int, input().split())))
    # 형식에 맞춰 최종값 출력
    print(f'#{_} {result}')

