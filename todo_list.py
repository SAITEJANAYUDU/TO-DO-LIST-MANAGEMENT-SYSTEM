tasks = []

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("             TO-DO LIST MANAGER")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")
    print("="*50)

def get_next_task_id(tasks):
    """Generate next available task ID"""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(tasks):
    """Add a new task to the to-do list"""
    print("\n--- Add New Task ---")
    
    if len(tasks) >= 8:
        print(" Maximum task limit reached (8 tasks)")
        print("Please complete or delete some tasks before adding new ones.")
        return tasks
    
    task_description = input("Enter task description: ").strip()
    if not task_description:
        print(" Task description cannot be empty")
        return tasks
    
    new_task = {
        "id": get_next_task_id(tasks),
        "task": task_description,
        "status": "Pending"
    }
    
    tasks.append(new_task)
    print(f" Task '{task_description}' added successfully!")
    print(f" Total tasks: {len(tasks)}/8")
    
    return tasks

def view_tasks(tasks):
    """Display all tasks with their status"""
    print("\n--- Your To-Do List ---")
    
    if not tasks:
        print(" No tasks found. Your to-do list is empty!")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'Status':<10} {'Task Description':<50}")
    print("-" * 70)
    
    pending_count = 0
    completed_count = 0
    
    for task in tasks:
        status_icon = "" if task["status"] == "Done" else "Pending"
        print(f"{task['id']:<5} {status_icon} {task['status']:<8} {task['task']:<50}")
        
        if task["status"] == "Done":
            completed_count += 1
        else:
            pending_count += 1
    
    print("=" * 70)
    print(f" Total Tasks: {len(tasks)}/8")
    print(f" Pending: {pending_count} |  Completed: {completed_count}")
    
    if len(tasks) > 0:
        progress = (completed_count / len(tasks)) * 100
        print(f" Progress: {progress:.1f}% completed")
    
    if completed_count == len(tasks) and len(tasks) > 0:
        print(" Amazing! All tasks completed! You're doing great!")
    elif progress >= 75:
        print(" Almost there! Keep up the good work!")
    elif progress >= 50:
        print(" Good progress! You're halfway there!")
    elif progress > 0:
        print(" You've started! Keep going!")

def find_task_by_id(tasks, task_id):
    """Find task by ID"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def update_task(tasks):
    """Update task description"""
    print("\n--- Update Task ---")
    
    if not tasks:
        print(" No tasks to update")
        return tasks
    
    view_tasks(tasks)
    
    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print(" Please enter a valid task ID number")
        return tasks
    
    task_to_update = find_task_by_id(tasks, task_id)
    if not task_to_update:
        print(" Task not found with the given ID")
        return tasks
    
    print(f"\nCurrent task: '{task_to_update['task']}'")
    print(f"Current status: {task_to_update['status']}")
    
    new_description = input("\nEnter new task description: ").strip()
    if not new_description:
        print(" Task description cannot be empty")
        return tasks
    
    old_description = task_to_update["task"]
    task_to_update["task"] = new_description
    print(f" Task updated successfully!")
    print(f"   From: '{old_description}'")
    print(f"   To:   '{new_description}'")
    
    return tasks

def mark_done(tasks):
    """Mark a task as completed"""
    print("\n--- Mark Task as Done ---")
    
    if not tasks:
        print(" No tasks to mark as done")
        return tasks
    
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    if not pending_tasks:
        print(" All tasks are already completed!")
        return tasks
    
    print("\nPending Tasks:")
    print("=" * 60)
    print(f"{'ID':<5} {'Task Description':<50}")
    print("-" * 60)
    for task in pending_tasks:
        print(f"{task['id']:<5} {task['task']:<50}")
    print("=" * 60)
    
    try:
        task_id = int(input("\nEnter task ID to mark as done: "))
    except ValueError:
        print(" Please enter a valid task ID number")
        return tasks
    
    task_to_complete = find_task_by_id(tasks, task_id)
    if not task_to_complete:
        print(" Task not found with the given ID")
        return tasks
    
    if task_to_complete["status"] == "Done":
        print(" This task is already completed!")
        return tasks

    task_to_complete["status"] = "Done"
    print(f" Task '{task_to_complete['task']}' marked as completed!")
    
    remaining_pending = len([task for task in tasks if task["status"] == "Pending"])
    if remaining_pending == 0:
        print(" Congratulations! All tasks completed")
    
    return tasks

def delete_task(tasks):
    """Delete a task from the list"""
    print("\n--- Delete Task ---")
    
    if not tasks:
        print(" No tasks to delete")
        return tasks
    
    view_tasks(tasks)
    
    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print(" Please enter a valid task ID number")
        return tasks
    
    task_to_delete = find_task_by_id(tasks, task_id)
    if not task_to_delete:
        print(" Task not found with the given ID")
        return tasks
    
    print(f"\n  Are you sure you want to delete this task?")
    print(f"   Task: '{task_to_delete['task']}'")
    print(f"   Status: {task_to_delete['status']}")
    confirmation = input("Type 'YES' to confirm deletion: ").strip().upper()
    
    if confirmation == "YES":
        tasks = [task for task in tasks if task["id"] != task_id]
        print(f" Task deleted successfully!")
        print(f" Remaining tasks: {len(tasks)}/8")
    else:
        print(" Deletion cancelled")
    
    return tasks

def display_task_statistics(tasks):
    """Display task statistics"""
    if not tasks:
        return
    
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task["status"] == "Done"])
    pending_tasks = total_tasks - completed_tasks
    
    print(f"\n Quick Stats: {completed_tasks}/{total_tasks} tasks completed")
    
    if total_tasks > 0:
        progress = (completed_tasks / total_tasks) * 100
        bar_length = 20
        filled_length = int(bar_length * completed_tasks // total_tasks)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        print(f" Progress: [{bar}] {progress:.1f}%")

def add_sample_tasks(tasks):
    """Add sample tasks for testing"""
    sample_tasks = [
        {"id": 1, "task": "Complete Python project", "status": "Pending"},
        {"id": 2, "task": "Buy groceries", "status": "Pending"},
        {"id": 3, "task": "Call dentist for appointment", "status": "Done"},
        {"id": 4, "task": "Read 30 pages of book", "status": "Pending"}
    ]
    
    for task in sample_tasks:
        if len(tasks) < 8:
            tasks.append(task)
    
    print(" Sample tasks added for testing")
    return tasks

def menu():
    """Main menu function to handle user interactions"""
    global tasks
    
    
    while True:
        display_menu()
        display_task_statistics(tasks)
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print(" Please enter a valid number (1-6)")
            continue
        
        if choice == 1:
            tasks = add_task(tasks)
        
        elif choice == 2:
            view_tasks(tasks)
        
        elif choice == 3:
            tasks = update_task(tasks)
        
        elif choice == 4:
            tasks = mark_done(tasks)
        
        elif choice == 5:
            tasks = delete_task(tasks)
        
        elif choice == 6:
            if tasks:
                pending_tasks = len([task for task in tasks if task["status"] == "Pending"])
                if pending_tasks > 0:
                    print(f"\n  You have {pending_tasks} pending task(s) remaining!")
            
            print("\n Thank you for using To-Do List Manager!")
            print(" Stay productive and organized!")
            break
        
        else:
            print(" Invalid choice. Please select 1-6")

if __name__ == "__main__":
    print(" To-Do List Management System")
    print(" Maximum capacity: 8 tasks")
    print(" Track your progress and stay organized!")
    print(" No data persistence - tasks lost on exit")
    
    menu()