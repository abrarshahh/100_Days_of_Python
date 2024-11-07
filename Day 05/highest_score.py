#highest score

scores = input("Input a List of Student Scores: ").split()

for n in range(0, len(scores)):
  scores[n] = int(scores[n])

highScore = 0
for score in scores:
  if score > highScore:
    highScore = score

print(f"The highest score in the class is: {highScore}")