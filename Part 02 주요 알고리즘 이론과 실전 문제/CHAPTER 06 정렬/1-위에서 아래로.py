# ((문제))
# 수열을 내링ㅁ차순으로 정렬하는 프로그램을 만드시오.

# (입력)
# 3
# 15
# 27
# 12

# (출력)
# 27 15 12

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse=True)

for number in numbers:
    print(number, end=" ")
