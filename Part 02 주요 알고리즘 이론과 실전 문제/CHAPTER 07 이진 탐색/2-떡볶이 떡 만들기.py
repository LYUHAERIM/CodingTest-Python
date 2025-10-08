# ((문제))
# 절단기를 이용하여 떡을 자를 것이다
# 예를 들면 19, 14, 10, 17을 절단기 15 높이로 자르면 15, 14, 10, 15가 된다
# 손님이 왔을 때 요청한 총 길이가 M일 때 절단기의 최대 높이를 구하시오

# (입력)
# 4 6
# 19 15 10 17

N, M = map(int, input().split())
tteok = list(map(int, input().split()))


def binary(array, target, start, end):
    mid = (start + end) // 2
    if mid - array == target:
        return print(mid)
    elif mid - array > target:
        return binary(array, target, start, mid - 1)
    else:
        return binary(array, target, mid + 1, end)


for i in range(N):
    result = binary(tteok, M, 0, max(tteok))
