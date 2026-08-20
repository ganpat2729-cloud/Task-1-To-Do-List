task = []

def main():
    print("---\n to-Do list\n---")
    while True:
        print("1. add task\n2. remove task\n3. view tasks\n4. mark task as done\n5. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_newtask()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

# Create a global variable for the ID counter at the top of your script
current_id = 1 

def add_newtask():
    global current_id
    new_task = input("Enter the new task: ")
    
    # Dictionary -> Table Row
    task_row = {
        "id": current_id,
        "task_name": new_task,
        "status": "Pending"
    }
    
    task.append(task_row)
    print(f"Task '{new_task}' added successfully with ID {current_id}.")
    current_id += 1


def remove_task():
    if task:
        print("Tasks:")
        for t in task:
            print(f"{t['id']}. {t['task_name']} [{t['status']}]")
        try:
            task_id = int(input("Enter the task ID to remove: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        for t in task:
            if t["id"] == task_id:
                task.remove(t)
                print(f"Task '{t['task_name']}' removed successfully.")
                return
        print("Invalid task ID.")
    else:
        print("No tasks to remove.")            



def view_tasks():
    if task:
        print("Tasks:")
        for t in task:
            print(f"{t['id']}. {t['task_name']} [{t['status']}]")
    else:
        print("No tasks to display.")


def mark_done():
    if task:
        for t in task:
            print(f"{t['id']}. {t['task_name']} [{t['status']}]")
        try:
            task_id = int(input("Enter the task ID to mark as done: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        for t in task:
            if t["id"] == task_id:
                t["status"] = "Done"
                print(f"Task '{t['task_name']}' marked as done.")
                return
        print("Invalid task ID.")
    else:
        print("No tasks to update.")


def exit_program():
    print("Exiting...")
    exit()

if __name__ == "__main__":
    main()
