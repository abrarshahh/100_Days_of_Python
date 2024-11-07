#Average height

student_heights = input("Write the list of student heights: \n").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for height in student_heights:
  sum_height += height

number_of_students = 0
for student in student_heights:
  number_of_students += 1

average_height = round(sum_height / number_of_students)
print(average_height)
  

