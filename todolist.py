tasks = []
def menu():
    print("\nTODO LIST APPLICATION")
    print("1. Add Task")
    print("2. Update Task")
    print("3. List Tasks")
    print("4. Quit")
def add():
    task = input("Enter the Task: ")
    tasks.append(task)
    print("TASK added successfully!")
def update():
    if not tasks:
        print("There is NO TASK to update.")
        return

    print("Current Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    task = int(input("Enter the task number to update: "))
    
    if 1 <= task <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid TASK number.")
def list():
    if not tasks:
        print("There is no TASK yet.")
    else:
        print("TODO LIST:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
while True:
    menu()
    option = int(input("Enter your Option: "))

    if option == 1:
        add()
    elif option == 2:
        update()
    elif option == 3:
        list()
    elif option == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")