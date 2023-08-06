num_of_student = input("Enter makes of student : ").split()
for n in range(len(num_of_student)):
    num_of_student[n] = int(num_of_student[n])
num_of_student.sort()
print(num_of_student)
print(f"The highier num is {num_of_student[-1]}")

