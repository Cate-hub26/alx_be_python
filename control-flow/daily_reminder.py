task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {'task_description'} is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"{'task_description'} is a low priority task. consider completing it when you have free time.")
        