import sys
sys.stdin = open('input.txt')
''' 배열 전체를 순회하면서 si, sj 수익 비용 비교
수익 >= 비용 최대 집의 수
1. 전체를 순회하면서 크기를 변경해보면서 완전탐색
2. 큐를 만듬 각 k 좌표를 거리에 따라 1,2,3 처럼 값을 넣음
bfs로 순회 4방향, 범위 내, 중복 x 그 위치에 집이 있으면 cnt +1
3. 모든 좌표에서 각 집까지의 거리(d= abs(si-ci) + abs(sj-cj) +1)형식
를 측정하고 각 좌표가 각 거리마다 가지는 집의 수를 세어놓음 그 거리로
k내 들어갈 집을 측정 가능함
'''

for tc in range(1, int(input()) + 1):
    result = 0
    print(f'#{tc} {result}')