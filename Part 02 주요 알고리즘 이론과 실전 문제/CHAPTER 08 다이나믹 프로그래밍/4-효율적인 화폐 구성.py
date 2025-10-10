# ((문제))
# N 종류의 화폐의 개수를 최소화하여 합이 M원이 되도록 만드시오

# (입력)
# 2 15
# 2
# 3


n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
dp[0] = 0

for coin in money:
    for i in range(coin, m + 1):
        dp[i]  = min(dp[i], dp[i - coin] + 1)


print(dp[i] if dp[i] != 0 else -1)
