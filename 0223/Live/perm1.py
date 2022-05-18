def f(i, N, r):
    if i==N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, r)
            p[i], p[j] = p[j], p[i]

N = 4
p = [x for x in range(1, N+1)]
f(0, N, 2)