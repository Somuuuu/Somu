users = {("john", "1234"): "admin", ("alice", "abcd"): "editor"}
username = input("Enter username: ")
password = input("Enter Password: ")
login = (username, password)
if login in users:
    role = users[(login)]
    print(f"Welcome, {role}")
else:
    print("Invalid login")
