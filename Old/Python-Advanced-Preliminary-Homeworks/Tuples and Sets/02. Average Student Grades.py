def add_grades(number):
    all_grades = {}
    for _ in range(number):
        name, grade = input().split()
        grade = float(grade)
        if name not in all_grades:
            all_grades[name] = []
        all_grades[name].append(grade)
    return all_grades


def print_result(grade_dict):
    for name, grades in grade_dict.items():
        avg = sum(grades) / len(grades)
        print(f'{name} -> {" ".join([f"{g:.2f}" for g in grades])} (avg: {avg:.2f})')


print_result(add_grades(int(input())))