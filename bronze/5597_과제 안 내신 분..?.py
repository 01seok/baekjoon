students = set(range(1, 31))

for _ in range(28):
    submitted = int(input())
    students.remove(submitted)

missing = sorted(students)
print(missing[0])
print(missing[1])