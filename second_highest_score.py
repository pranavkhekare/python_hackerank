def second_low(list):
    student_score_list = [i[1] for i in list]
    second_smallest_score = sorted(set(student_score_list))[1]
    student_score = [j for j, x in list if x == second_smallest_score]
    return student_score


student = []
for i in range(int(input())):
    name = input()
    score = float(input())
    student.append([name, score])

second_score = second_low(student)
for names in sorted(second_score):
    print(names)