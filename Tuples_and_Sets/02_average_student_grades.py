n = int(input())
students = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for s, g in students.items():
    avg = sum(g) / len(g)
    print(f'{s} -> {" ".join([f"{x:.2f}" for x in g])} (avg: {avg:.2f})')