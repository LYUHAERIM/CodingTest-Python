# ((문제))
# 개미 전사가 들키지않고 식량창고를 약탈하기 위해서는 최소한 한칸 이상 떨어진 식량창고를 약탈해야한다

# (입력)
# 4
# 1 3 1 5

# (출력)
# 8

N = int(input())
food = list(map(int, input().split()))

if N == 1:
    print(food[0])
else:
    best = [0] * N
    best[0] = food[0]
    best[1] = max(food[0], food[1])
    for i in range(2, N):
        best[i] = max(best[i - 1], best[i - 2] + food[i]) #best[2] = max(best[1], best[0] + food[2])
    print(best[-1])
