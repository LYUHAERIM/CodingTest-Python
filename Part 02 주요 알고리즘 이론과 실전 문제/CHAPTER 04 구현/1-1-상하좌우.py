# ((문제))
# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져있다
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다
# 우리 앞에는 여행가 A가 이동할 게획이 적힌 계획서가 놓여있다

# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동

# (입력)
# 5
# R R R U D D

# (출력)
# 3 4

N = int(input())
move = list(map(str, input().split()))

startX = 1
startY = 1

for i in range(len(move)):
    if move[i] == "R":
        if startX + 1 < N:
            startX += 1
    if move[i] == "L":
        if startX - 1 > 0:
            startX -= 1
    if move[i] == "U":
        if startY - 1 > 0:
            startY -= 1
    if move[i] == "D":
        if startY + 1 < N:
            startY += 1

print(startY, startX)
