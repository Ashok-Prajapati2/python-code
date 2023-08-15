student_hight = input("Enter student hight : ").split()
len_student_hight = int(len(student_hight))
# print(len_student_hight)

a = 0
for n in range(len_student_hight):
    student_hight[n] = int(student_hight[n])
    # second method
    
    a += int(student_hight[n])
    avg_is = a/len_student_hight
   
print(f"Avg of the student hight is : {avg_is}")

# print(student_hight)
sum_hight = sum(student_hight)
# print(sum_hight)
avg = int(sum_hight)/int(len_student_hight)

print(f"Avg of the student hight is : {avg}")
  