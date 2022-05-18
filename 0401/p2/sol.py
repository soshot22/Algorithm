import sys
sys.stdin = open('input.txt')

def BFS(v):
    queue = []
    visitied = [0]*8
    visitied[v] = 1
    queue.append(v)
    print(v, end='')
    while queue:
        s = queue.pop(0)
        for i in range(1, 8):
            if i in arr[s] and visitied[i] == 0:
                queue.append(i)
                visitied[i] = 1
                print(f'-{i}', end='')

arr = [[] for _ in range(8)]
links = list(map(int, input().split()))
for i in range(len(links)//2):
    n1, n2 = links[i*2], links[i*2 +1]
    arr[n1] += [n2]
    arr[n2] += [n1]
BFS(1)
