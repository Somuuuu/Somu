tags = {"python", "fastapi", "backend"}
a = input("Enter a new tag: ")
if a in tags:
    print("Tag already exists.")
else:
    tags.add(a)
    print(tags)