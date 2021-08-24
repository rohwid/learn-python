student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

# Print keys only
for student in student_attendance:
    print(student)

# Print keys and value
for student in student_attendance:
    print(f'{student}: {student_attendance[student]}')

# Print keys and value like enumerate
for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')