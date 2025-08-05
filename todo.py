class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
            return
        print("\nYour TODO List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Marked task {task_index} as completed!")
        else:
            print("Invalid task number!")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number!")

def main():
    todo = TodoList()
    while True:
        print("\n=== TODO List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter task description: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_num)
        elif choice == "4":
            todo.view_tasks()
            task_num = int(input("Enter task number to remove: "))
            todo.remove_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()