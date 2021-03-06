#캔디팡
from collections import deque

array = [list(map(int, input().split())) for _ in range(7)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
result = 0
def bfs(x, y):
    cnt = 1
    global result
    q = deque()
    q.append((x, y))
    target = array[x][y]
    array[x][y] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < 7 and ny < 7:
                if array[nx][ny] == target:
                    array[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
        if cnt >= 3:
            result += 1
    if cnt >= 3:
        result += 1


for a in range(7):
    for b in range(7):
        if array[a][b] != 0:
            bfs(a, b)
print(result)                    


