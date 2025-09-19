import time

start_time = time.time()

# ((문제))
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스(번호)에 대항하는 수가 연속해서 K번을 초과하여 더해질 수 없다

# 배열의 크기 N
# 숫자가 더해지는 횟수 M
# 연속 가능 횟수 K

# (입력)
# 5 8 3
# 2 4 5 4 6

# (출력)
# 46

# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)  # 입력받은 수들 정렬하기
sum = 0

while M > 0:
    for i in range(K):
        sum += data[0]
        M -= 1
    sum += data[1]
    M -= 1

print(sum)

end_time = time.time()

print(start_time - end_time)
