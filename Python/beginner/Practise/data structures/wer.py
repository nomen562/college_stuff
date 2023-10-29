# Use Dictionary to store the student’s information (name, roll number,
# marks-CAT, quiz, DA, FAT for five subjects) and obtain the grade of
# the student.
name, roll_no = input("Enter your name>"), int(input("Enter your roll no>"))
l = ['CAT out of 50', 'quiz out of 10', 'DA out of 10', 'FAT out of 100']
marks = [[0, 0, 0, 0]]*5

for x in range(5):
    for y in range(4):
        marks[x][y] = int(input(f"For subject_{x+1} enter marks in {l[y]}>"))


def grade(n):
    if n <= 0.5:
        return "F Grade"
    elif n <= 0.7:
        return "D Grade"
    elif n <= 0.8:
        return "C Grade"
    elif n <= 0.9:
        return "B Grade"
    else:
        return "A Grade"


dick = {'name': name, 'Roll_No': roll_no, 'marks': marks}
# Now obtaining grade
# grade = 0.3(CAT) + 0.1(quiz) + 0.1(DA) + 0.5(FAT)
c = 1
print(f"Your name is>{dick['name']}\nRoll number is>{dick['Roll_No']}")
for i in dick["marks"]:
    grad = 0.3*i[0]/50 + 0.1*i[1]/10 + 0.1*i[2]/10 + 0.5*i[3]/100
    print(f"Grade in Subject_{c}>{grade(grad)}")
    c += 1
