tasks = []  # Each task will be a dict: {"title": str, "done": bool}

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def add_task():
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to mark done: "))
            tasks[num - 1]["done"] = True
            print("Task marked as done!")
        except (ValueError, IndexError):
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed['title']}")
        except (ValueError, IndexError):
            print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Try again.")
