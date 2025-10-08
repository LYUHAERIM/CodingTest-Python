# ((문제))
# 두 개의 배열 A, B는 N개의 원소로 이루어져있다
# 최대 K번의 바꿔치기를 통해 A 원소와 B 원소를 바꿀 수 있다
# A의 원소의 합이 최대가 되도록 작성하시오

# N, K = map(int, input().split())
# arrayA = list(map(int, input().split()))
# arrayB = list(map(int, input().split()))

# arrayA.sort()
# arrayB.sort()
# arrayC = []

# for i in range(K):
#     sumArray = sum(arrayA[K - i :] + arrayB[N - K + i :])
#     arrayC.append(sumArray)

# arrayC.sort()
# print(arrayC[-1])

N, K = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort(reverse=True)
arrayB.sort()

print(arrayA, arrayB)

for i in range(K):
    if arrayA[N - K + i] <= arrayB[N - K + i]:
        arrayA[N - K + i] = arrayB[N - K + i]

print(sum(arrayA))
