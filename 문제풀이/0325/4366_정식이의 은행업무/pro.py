import sys
sys.stdin = open('input.txt')

# 이진수 1자리씩 변경 > 10진 > 3진수로 변경
# 이진수를 변경하여 만든 3진수와 기존 3진수가 1자리만 틀리면 됨

def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i] + 1) % 2
        dec = 0
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]
        # 10진수를 3진수 변환
        s = []
        # 3으로 계속 나눔
        ret = dec
        while dec > 0:
            # 낮은 자리가 앞에 오도록
            s.append(dec % 3)
            dec //= 3
        # 비교할 수고 뒤로 바꾼 것이므로 기준문자도 좌우변경
        lst3 = lst3[::-1]
        cnt = 0
        # 만약 변환 진법수와 입력 진법의 자릿수가 틀리수도 있으니
        for idx in range(min(len(lst3), len(s))):
            if s[idx] != lst3[idx]:
                cnt += 1
        cnt += abs(len(lst3) - len(s))
        # 한 자리만 다르므로
        if cnt == 1:
            return ret
        # 2진수 1비트 바꾼 값 원상 복귀
        lst2[i] = (lst2[i] + 1) % 2
            


for tc in range(1, int(input()) + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    # 3진법 리스트만 좌우 바꿔야 하므로
    ans = solve(lst3)
    print(f'#{tc} {ans}')