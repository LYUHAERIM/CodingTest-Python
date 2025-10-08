# ((문제))
# N개 부품을 입력받고
# M개 부품이 있는지 없는지 출력하는 프로그램을 작성하시오

# (입력)
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# (출력)
# no yes yes

N = int(input())
listN = list(map(int, input().split()))

M = int(input())
listM = list(map(int, input().split()))


def binary(array, target, start, end):
    if start > end:
        return print("no", end=" ")
    mid = (start + end) // 2
    if array[mid] == target:
        return print("yes", end=" ")
    elif mid > target:
        return binary(array, target, start, mid - 1)
    else:
        return binary(array, target, mid + 1, end)


print(listN, listM)

for i in range(M):
    result = binary(listN, listM[i], 0, N - 1)
