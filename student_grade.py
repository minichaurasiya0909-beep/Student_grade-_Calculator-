print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter your name: ")
num_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / num_subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Name:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)

save = input("\nSave result? (yes/no): ")

if save.lower() == "yes":
    file = open("result.txt", "a")
    file.write(f"\nName: {name}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Percentage: {percentage}\n")
    file.write(f"Grade: {grade}\n")
    file.write("------------------\n")
    file.close()

    print("Saved successfully!")
