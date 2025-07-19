task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timed = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if timed == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority}  is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if timed == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority}  is a low priority task. Consider completing it when you have free time.")
    case "low":
        if timed == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority}  is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use: high, medium, or low.")
