tasks=[]
while True:
        print("\n1.Display to-do list")
        print("2.Add a task")
        print("3.Mark a task as completed")
        print("4.Remove a task")
        print("5.Quit")

        choice = input("Enter your choice: ")
        if choice=='1':
          if len(tasks)==0:
           print("No tasks available")
          else:
           print("Tasks:  ")
           for task in tasks:
            print("-"+task)
        elif choice=='2':
            task=input("Enter task: ")
            tasks.append(task)
            print("Task added")
        elif choice == '3':
         if len(tasks) == 0:
          print("No tasks available")
         else:
           for i in range(len(tasks)):
            print(i+1, ".", tasks[i])
         num = int(input("Enter task number: "))
         if num >= 1 and num <= len(tasks):
            tasks[num-1] += " (Completed)"
            print("Task marked as completed")
         else:
            print("Invalid task number")
        elif choice=='4':
          task=input("Enter task to remove:")
          if task in tasks:
            tasks.remove(task)
            print("Task removed")
          else:
            print("Task not found")
        elif choice=='5':
          print("Existing...")
          break
        else:
         print("Invalid choice")
