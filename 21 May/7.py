students = {
   "alice": (85, 90, 78),
   "bob": (50, 45, 60)
}
name = input("Enter student name: ")
if name == "alice":
    a = sum(students["alice"])/len(students["alice"])
    if a >=60:
        print("Passed")
elif name == "bob":
    b = sum(students["bob"])/len(students["bob"])
    if b < 60: 
        print("failed")
else:
    print("Student not found")