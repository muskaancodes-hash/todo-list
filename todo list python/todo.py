print("===== TO-DO LIST =====")
print("1. Add Task")
print("2. Remove Task")
print("3. View Task")
print("4. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    print("\n--- Add New Task ---")
    task = input("Enter task name: ")

    if task:
        task.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
