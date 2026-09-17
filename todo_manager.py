# interactive to-do list manager
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

print("=" * 40)
print("        TO-DO LIST")
print("=" * 40)

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

choice = input("\nEnter 1 to add a task or 2 to remove a task: ")

if choice == "1":
    tasks.append(input("Add a new task: "))
    print("\nUpdated To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
elif choice == "2":
    try:
        task_number = int(input("Enter the task number to remove: "))
        index = task_number - 1

        if index < 0 or index >= len(tasks):
            raise IndexError("Task number out of range.")

        removed_task = tasks.pop(index)
        print(f"Task removed: {removed_task}")
        print("\nUpdated To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    except (ValueError, IndexError) as e:
        print(f"\nInvalid input: {e}. Please enter a valid task number.")
    print("\nCurrent To-Do List:")
else:
    print("\nInvalid choice.")

    #display the current tasks
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

    # display total number of remaining tasks
print(f"\nTotal tasks remaining: {len(tasks)}")
