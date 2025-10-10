# ((문제))
# 절단기를 이용하여 떡을 자를 것이다
# 예를 들면 19, 14, 10, 17을 절단기 15 높이로 자르면 15, 14, 10, 15가 된다
# 손님이 왔을 때 요청한 총 길이가 M일 때 절단기의 최대 높이를 구하시오

# (입력)
# 4 6
# 19 15 10 17

# (출력)
# 15

N, M = map(int, input().split())
tteok = list(map(int, input().split()))


# 절단기 높이를 조절, 최대 높이를 도전
def binary(array, need):
    lo, hi = 0, max(array)
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cut_sum = 0
        for i in array:
            if mid < i:
                cut_sum += i - mid
        if cut_sum >= need:
            ans = mid
            lo = mid+1
        else:
            hi = mid -1
    return ans


result = binary(tteok, M)
print(result)
