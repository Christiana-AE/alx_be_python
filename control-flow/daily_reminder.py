task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timed = input("Is it time-bound? (yes/no): ")

match priority:
    case _:
        if timed == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        elif timed == "no":
            print(f"{priority}  is a low priority task. Consider completing it when you have free time.")
