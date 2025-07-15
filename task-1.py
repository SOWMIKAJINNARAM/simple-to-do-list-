# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✅ Done" if task['done'] else "❌ Not Done"
            print(f"{index}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "done": False})
    print("Task added!")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: ")) - 1
        if 0 <= task_no < len(todo_list):
            new_title = input("Enter new title: ")
            todo_list[task_no]['title'] = new_title
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            removed = todo_list.pop(task_no)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
