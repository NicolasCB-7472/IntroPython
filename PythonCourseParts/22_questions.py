import json
# List/dictionaries can be used for similar objects (see video)

with open("./PythonCourseParts/22_questions.json", 'r') as file_j:
    content = file_j.read()

data = json.loads(content)

score = 0
student_answer = []
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index +1, '-', alternative)
    user_choice = int(input("Please, enter the correct answer: "))
    student_answer.append(user_choice)
    if user_choice == question["correct_answer"]:
        score += 1

index = 0
for question in data:
  if(len(student_answer) > index):
    message = f"Your answer: {student_answer[index]}."
  message += f" Correct answer: {question['correct_answer']}"
  print(message)
  index += 1


#print(data)
print(score, '/', len(data))