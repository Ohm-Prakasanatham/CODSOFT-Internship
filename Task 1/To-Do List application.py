import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def update_task(self, task_id, new_task):
        if 0 <= task_id < len(self.tasks):
            old_task = self.tasks[task_id]
            self.tasks[task_id] = new_task
            print(f"Updated task {task_id} from '{old_task}' to '{new_task}'")
        else:
            print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            task = self.tasks.pop(task_id)
            print(f"Deleted task: {task}")
        else:
            print(f"Task ID {task_id} not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}: {task}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            to_do_list.view_tasks()
        elif choice == '2':
            clear_screen()
            task = input("Enter the task to add: ")
            to_do_list.add_task(task)
        elif choice == '3':
            clear_screen()
            to_do_list.view_tasks()
            try:
                task_id = int(input("Enter the task ID to update: "))
                new_task = input("Enter the new task: ")
                to_do_list.update_task(task_id, new_task)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            clear_screen()
            to_do_list.view_tasks()
            try:
                task_id = int(input("Enter the task ID to delete: "))
                to_do_list.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '5':
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
