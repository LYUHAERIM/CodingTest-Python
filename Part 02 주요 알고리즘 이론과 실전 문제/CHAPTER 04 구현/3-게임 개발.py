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
x, y, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# 방문 체크
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1

# 방향: 0:북(-1,0), 1:동(0,1), 2:남(1,0), 3:서(0,-1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left(d):
    return (d - 1) % 4


count = 1  # 방문한 칸 수
turn_time = 0  # 연속 회전 횟수(4가 되면 뒤로 이동 시도)

while True:
    # 1) 왼쪽으로 회전
    turn_left(d)
    d = turn_left(d)
    nx = x + dx[d]
    ny = y + dy[d]

    # 2) 왼쪽 방향 칸이 미방문 육지면 전진
    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 3) 네 방향 모두 가봤거나 바다라면 뒤로 이동
    if turn_time == 4:
        bx = x - dx[d]
        by = y - dy[d]
        #  뒤가 육지면 뒤로만 한 칸
        if 0 <= bx < N and 0 <= by < M and grid[bx][by] == 0:
            x, y = bx, by
            turn_time = 0
        else:
            # 뒤가 바다면 종료
            break

print(count)
