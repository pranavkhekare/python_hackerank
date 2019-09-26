n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for name, scores in student_marks.items():
    if name == query_name:
        print('%.2f' % ((scores[0] + scores[1] + scores[2])/3))