my_tasks = []

while True:
    print("\n------ TO DO LIST ------")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        task = input("Enter your task: ")
        my_tasks.append(task)
        print("Task Added!")

    elif option == "2":
        if my_tasks:
            print("\nYour Tasks:")
            count = 1
            for item in my_tasks:
                print(str(count) + ". " + item)
                count += 1
        else:
            print("Task list is empty.")

    elif option == "3":
        if my_tasks:
            count = 1
            for item in my_tasks:
                print(str(count) + ". " + item)
                count += 1

            delete = int(input("Enter task number: "))

            if delete >= 1 and delete <= len(my_tasks):
                my_tasks.pop(delete - 1)
                print("Task Deleted!")
            else:
                print("Wrong Number")
        else:
            print("No task found.")

    elif option == "4":
        print("Program Closed")
        break

    else:
        print("Please choose a valid option.")