tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)  # Use append to add the task to the list
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:  # Check the 'tasks' list
        print("There are no tasks currently.")
    else:
        print("Tasks are:")
        for index, task in enumerate(tasks):  # Use 'tasks' here
            print(f"Task number {index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)  # Remove the task from the list
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task number {taskToDelete} was not found.")
    except ValueError:  # Catch invalid input
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the TO DO list app!")
    while True:
        print("\nPlease select one of the following options:")
        print("1. Add a new task")
        print("2. List tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask() #function name
        elif choice == "2":
            listTasks()  
        elif choice == "3":
            deleteTask()
        elif choice == "4":
            print("Thank you and goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
