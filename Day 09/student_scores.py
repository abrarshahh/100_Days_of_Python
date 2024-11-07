#student scores

student_scores = {
  "Sharik": 81,
  "Abrar": 71,
  "Aseeb": 99,
  "Ruvaid": 97,
  "Basit": 83,
  "Adnan": 85,
  "Shayan": 90,
}

student_grades = {}

for student in student_scores:
  if student_scores[student] >= 91:
    student_grades[student] = "Outstanding"

  elif student_scores[student] >= 81:
    student_grades[student] = "Exceeds Expectation"

  elif student_scores[student] >= 71:
    student_grades[student] = "Acceptable"

  else:
    student_grades[student] = "Fail"

print(student_grades)