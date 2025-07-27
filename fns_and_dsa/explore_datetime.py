import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    new_date = current_date + datetime.timedelta(days= number_of_days)
    formatted_new_date = new_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_new_date}")