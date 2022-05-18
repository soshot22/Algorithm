import sys
sys.stdin = open('input.txt')

# BFS 탐색으로 모든 경우의 수 
def BFS(n, ssum):
    global result
    # 12번째 해를 넘는다면(0~11번째까지 12개가 선택된 상황)
    if n >= 13:
        # 현재 이용료가 결과보다 더 작다면 교체
        if ssum < result:
            result = ssum
        return
    # 하루로 해당 달을 계산하는 경우 +1
    BFS(n + 1, ssum + arr[n]*day)
    # 월이용료로 달을 선택한 경우 +1
    BFS(n+ 1, ssum + month)
    # 세달 이용료로 시작하면 +3
    BFS(n+ 3, ssum + three)
    # 한해 이용료를 한 경우 +12
    BFS(n+ 12, ssum + year)


for tc in range(1, int(input()) + 1):
    # 각각 이용료 변수 입력
    day, month, three, year = map(int, input().split())
    # 리스트로 만들기
    arr = list(map(int, input().split()))
    # 리스트를 1부터 사용하기 위해 0 추가
    arr.insert(0, 0)
    # 임의의 큰수 생성
    result = year * 20
    # 시작달과 이용료 시작 0원 입력
    BFS(1, 0)
    print(f'#{tc} {result}')