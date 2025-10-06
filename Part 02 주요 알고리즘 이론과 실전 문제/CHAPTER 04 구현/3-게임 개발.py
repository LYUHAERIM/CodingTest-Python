# ((문제))
# N X M 직사각형, 0 육지 1 바다
# 1. 현재 위치에서 왼쪽 방향으로 한 칸 이동
# 2. 왼쪽 방향에 가보지 않은 칸이 존재하면 왼쪽으로 회전한 다음 이동, 가보지 않은 곳이 없다면 왼쪽으로 방향만 이동
# 3. 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 방향을 유지한 채로 뒤로 한칸 이동 후 1단계로 돌아간다
# (단, 뒤쪽 방향이 바다인 경우 멈춘다)

# 0: 북 / 1: 동 / 2: 남 / 3: 서

# 캐릭터가 방문한 칸의 수를 출력하시오

# (입력)
# 4 4               4 X 4 맵 생성
# 1 1 0             (1, 1)에서 북쪽(0)을 바라보고 서있음
# 1 1 1 1           
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

N, M = map(int, input().split())
x, y, dir = map(int, input().split())

maps = []
result = 1

for i in range(M):
    maps.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

used = [[0]*N for _ in range(M)]
used[x][y] = 1

for n in range(N):
    for m in range(M):
        for d in range(4):
            if 0<= n < N and 0<= m < M and maps[n][m] == 0 and used[n][m] == 0:
                nx = x + dx[d]
                ny = y + dy[d]
                used[n][m] = 1
                print('n, m', n, m)
                print('d', d)
                print('nx, ny', nx, ny)
                print('-------')
                result += 1


print(result)