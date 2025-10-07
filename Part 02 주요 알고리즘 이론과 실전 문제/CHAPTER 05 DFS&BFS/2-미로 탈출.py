# ((문제))
# N X M 미로
# 현재 위치 (1, 1) 출구 (N, M)
# 괴물이 있는 부분 1, 괴물이 없는 부분 0
# 탈출하기 위해 움직여야 하는 최소 칸의 개수

from collections import deque

N, M = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start_x, start_y = 0, 0 
distance = 1
end_x, end_y = N - 1, M - 1

q = deque()
q.append((start_x, start_y, distance))

visited = set()
visited.add((start_x, start_y))

while q:
    x, y, distance = q.popleft()
    if (x, y) == (end_x, end_y):
        break
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and map[nx][ny] == 1:
            q.append((nx, ny, distance + 1))
            visited.add((nx, ny))

print(distance)
