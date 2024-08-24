# todo_list.py

import json
import datetime

# Load task data from JSON file
def load_tasks():
    try:
        with open('data.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save task data to JSON file
def save_tasks(tasks):
    with open('data.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Create a new task
def create_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high, medium, low): ")
    task = {
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task created!")

# List all tasks
def list_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i}. {task['description']} - {task['due_date']} - {task['priority']} - {status}")

# Update a task
def update_task(tasks):
    task_id = int(input("Enter task ID to update: ")) - 1
    if task_id < 0 or task_id >= len(tasks):
        print("Invalid task ID")
        return
    task = tasks[task_id]
    description = input("Enter new task description (or press enter to keep current): ")
    if description:
        task['description'] = description
    due_date = input("Enter new due date (or press enter to keep current): ")
    if due_date:
        task['due_date'] = due_date
    priority = input("Enter new priority (or press enter to keep current): ")
    if priority:
        task['priority'] = priority
    save_tasks(tasks)
    print("Task updated!")

# Complete a task
def complete_task(tasks):
    task_id = int(input("Enter task ID to complete: ")) - 1
    if task_id < 0 or task_id >= len(tasks):
        print("Invalid task ID")
        return
    task = tasks[task_id]
    task['completed'] = True
    save_tasks(tasks)
    print("Task completed!")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: ")) - 1
    if task_id < 0 or task_id >= len(tasks):
        print("Invalid task ID")
        return
    del tasks[task_id]
    save_tasks(tasks)
    print("Task deleted!")

# Search for tasks
def search_tasks(tasks):
    query = input("Enter search query: ")
    results = [task for task in tasks if query in task['description']]
    if results:
        print("Search results:")
        for i, task in enumerate(results, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['description']} - {task['due_date']} - {task['priority']} - {status}")
    else:
        print("No results found")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Menu:")
        print("1. Create task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Complete task")
        print("5. Delete task")
        print("6. Search tasks")
        print("7. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            search_tasks(tasks)
        elif choice == '7':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()