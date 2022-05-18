def f(i, N, K):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]
        if s == K:
            for j in range(N):
                if bit[j]:
                    print(a[j], end =' ')
            print()
    else:
        bit[i] = 1; f(i+1, N, K)
        bit[i] = 0; f(i+1, N, K)
    return
a = [i for i in range(1, 11)]
N = len(a)
K = 10
bit = [0] * N
f(0, 10, 10)
