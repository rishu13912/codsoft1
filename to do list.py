import json

# Function to load existing tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (high, medium, low): ")
    task = {
        'name': task_name,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{index + 1}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']}, Status: {status})")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
