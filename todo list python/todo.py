print("===== TO-DO LIST =====")
print("1. Add Task")
print("2. Remove Task")
print("3. View Task")
print("4. Exit")
tasks = []
choice = input("Enter your choice: ")

if choice == "1":
    print("\n--- Add New Task ---")
    task = input("Enter task name: ")      

    if task:
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
if choice == "1":
    print("\n--- Add New Task ---")
    task = input("Enter task name: ")

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
elif choice == "3":
    print("\nYour Tasks:")

    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)   
elif choice == "2":
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        print("\nYour Tasks:")

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        task_number = int(input("Enter task number to delete: "))

        if task_number >= 1 and task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print("Task deleted:", deleted_task)
        else:
            print("Invalid task number.") 