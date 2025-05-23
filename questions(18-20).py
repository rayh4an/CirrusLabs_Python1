print('Question 18\n')

def quiz():
    questions = [
        {
            "question": "What is 19 - 9?",
            "options": ["a) 10", "b) 9", "c) undefined", "d) 12"],
            "answer": "a"
        },
        {
            "question": "Which of the following is a language?",
            "options": ["a) Skill", "b) Heartness", "c) Dutch", "d) Corn"],
            "answer": "c"
        },
        {
            "question": "When did WW2 end?",
            "options": ["a) 1922", "b) 1945", "c) 1939", "d) 1942"],
            "answer": "b"
        }
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")

    print(f"\nYou scored {score}/{len(questions)}.")

quiz()


print('\nQuestion 19\n')

def expenseAdded(expense_log, day, amount):
    if day not in expense_log:
        expense_log[day] = []
    expense_log[day].append(amount)

def expenseWeekSum(expense_log):
    total = 0
    print("\nWeekly Expense Summary:")
    for day, expenses in expense_log.items():
        day_total = sum(expenses)
        total += day_total
        print(f"{day}: ${day_total:.2f}")
    print(f"Total Weekly Expenses: ${total:.2f}")

expenses = {}
expenseAdded(expenses, "Monday", 16)
expenseAdded(expenses, "Tuesday", 4.50)
expenseAdded(expenses, "Tuesday", 12.05)
expenseAdded(expenses, "Wednesday", 0)
expenseAdded(expenses, "Thursday", 43)
expenseAdded(expenses, "Friday", 8.75)

expenseWeekSum(expenses)


print('\nQuestion 20\n')

def tasksLoad(filename="tasks.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def tasksSave(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def tasksDisplay(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def toDo():
    tasks = tasksLoad()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            new_task = input("Enter task: ")
            tasks.append(new_task)
        elif choice == "2":
            tasksDisplay(tasks)
            idx = int(input("Enter task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
            else:
                print("Invalid task number.")
        elif choice == "3":
            tasksDisplay(tasks)
        elif choice == "4":
            tasksSave(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option.")


toDo()
