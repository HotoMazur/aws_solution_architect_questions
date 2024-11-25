import random

file = open("README.md", 'r')

questions = {}
current_question = 0
question = []
answers = []
answer = ""

lines = []

with open("questions.txt", 'r') as file:
    start_line = 854

    for current_line_number, line in enumerate(file, start=1):
        if current_line_number >= start_line:
            lines.append(line.strip())  # Add to list, stripping extra spaces or newlines

    lines.remove("")

    for count, line in enumerate(lines):
        if line.startswith("###"):
            if len(question) > 0:
                current_question += 1
                question.append(answers)
                question.append(answer)
                questions[current_question] = question
                question = [line]
                answers = []
            else:
                question = [line]
        elif line.startswith("- [ ]"):
            answers.append(line.removeprefix("- [ ]"))
        elif line.startswith("- [x]"):
            answers.append(line.removeprefix("- [x]"))
            answer = line.removeprefix("- [x]")


question = random.choice(questions)
points = 0
for _ in range(65):
    question = random.choice(questions)
    print(question[0])
    for num, answer in enumerate(question[1]):
        print(str(num + 1) + ": " + answer)
    print("")

    user_choose = input("Enter: ")
    while int(user_choose) > len(question[1]):
        user_choose = input("Incorrect answer, try again: ")
    if question[1][int(user_choose) - 1] == question[-1]:
        points += 1
        print("Correct")
    else:
        print("Incorrect")
        print(question[-1])

    print("############################################################")

print("")
print(str(int((points / 10) * 100)) + "%")