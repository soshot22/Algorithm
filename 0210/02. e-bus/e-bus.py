'''
[조건] 1. 버스 0 -> N 번 정류장 이동  2. 최대 이동 K
3. 충전기가 설치된 M개의 정류장 번호   4. 최소 충전 횟수
5. 충전기 설치가 잘못되어 종점 도달 x 시 0출력
6. 출발지는 충전 횟수x
[입력] 노선의 수 / K, N, M / M개의 정류장 번호
[출력] #{노선번호} {충전횟수 or 0}
'''
# input.txt 불러오기
import sys
sys.stdin = open('input.txt')
# 노선의 수 입력
T = int(input())
# 노선의 수만큼 반복
for tc in range(T):
    # KNM 각각 리스트로 받아 입력, K와 N만 사용
    KNM = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]
    # 충전소가 있는 위치 입력값, 충전소 배치 리스트
    charge_num = list(map(int, input().split()))
    charge_ls = [0] * (N + 1)
    # 0번째를 포함한 충전소 리스트 작성
    for charge in charge_num:
        charge_ls[charge] += 1
    # K범위 내에서 최댓값 찾기, 현위치, 충전횟수
    now = count = 0
    # 충전후 다시 가는 K가 목표 N보다 작으면 반복
    while now + K < N:
        # 현재위치에서 K사이 충전소 확인 변수
        far_charge = 0
        # K만큼 가는 동안 충전소가 있으면 뒤 충전소 저장
        for i in range(1, K + 1):
            if charge_ls[now + i] == 1:
                far_charge = i
        # 사이의 충전소가 있는 경우 위치 변경 및 충전횟수 증가
        if far_charge > 0:
            count += 1
            now = now + far_charge
        # 충전소가 사이에 없는 경우 충전횟수 0으로하고 반복문 종료
        else:
            count = 0
            break
    print(f'#{tc + 1} {count}')






