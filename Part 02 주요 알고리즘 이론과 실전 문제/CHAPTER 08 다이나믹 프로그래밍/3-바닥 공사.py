# ((문제))
# 가로 길이 N, 세로 길이 2인 직사각형
# 1 X 2, 2 X 1, 2 X 2를 이용하여 채울 수 있는 모든 경우의 수를 구하시오
# (796,796으로 나눈 니머지를 출력하세요)


n = int(input())

best = [0] * (n + 1)

best[1] = 1
best[2] = 3
for i in range(3, n + 1):
    best[i] = (best[i - 1] + 2 * best[i - 2]) % 796796

print(best[n])
