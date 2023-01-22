tasks = []

while True:
    # Print the current tasks
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(i + 1, task)

    # Print the available options
    print("Enter a number to select an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")

    # Get the user's choice
    choice = int(input())

    # Add a task
    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
    # Remove a task
    elif choice == 2:
        task_index = int(input("Enter the number of the task to remove: "))
        if (task_index>=1) and (task_index<=len(tasks)):
            del tasks[task_index - 1]
        else:
            print("Invalid task number")
    elif choice == 3:
        break
    else:
        print("Invalid option selected")
