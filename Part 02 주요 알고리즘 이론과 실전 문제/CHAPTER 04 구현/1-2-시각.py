# ((문제))
# 정수 N이 입려되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
# ex) 3이 있는 경우 - 13분 30초, 3이 없는 경우 - 00시 02분 55초

# (입력)
# 5

# (출력)
# 11475

N = int(input())

result = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                result += 1

print(result)
