# ((문제))
# N X M 얼음틀
# 구멍 0 칸막이 1
# 생성되는 아이스크림의 총 개수

# (입력)
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# (출력)
# 8

from collections import deque

N, M = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(N)]

x, y = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

used = [[0] * M for _ in range(N)]

q = deque()
q.append((x, y))

used[x][y] = 1
count = 0

while q:
    x, y = q.popleft()

    for n in range(N):
        for m in range(M):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and used[n][m] == 0:
                    q.append((nx, ny))
                    used[n][m] = 1
                    count += 1


print(count)
