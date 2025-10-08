# ((문제))
# N명의 학생정보는 이름과 성적으로 구분된다
# 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오

# (입력)
# 2
# 홍길동 95
# 이순신 77

# (출력)
# 이순신 홍길동

N = int(input())
array = []
for _ in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=" ")
