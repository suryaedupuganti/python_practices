from calendar import month, week


# print("this is practice")
# print(28)
# print("today is may " + str(25) + " day")
# print(f"today is may {25} day")
# print(25 * 24 * 60)
# count_of_hours_in_day = 24
# print(f"the hours of 25 days are {25 * count_of_hours_in_day} is true")
# print(f"the hours of 30 days are {30 * count_of_hours_in_day} is true")
# print(f"the hours of 40 days are {40 * count_of_hours_in_day} is true")
# print(f"the hours of 50 days are {50 * count_of_hours_in_day} is true")
# print(f"the hours of 100 days are {100 * count_of_hours_in_day} is true")
# print(40+40)
# adding_of_two_digits = 40+40
# print(f"the result is = {20+adding_of_two_digits} ")

# Functions

Calculation_of_days_for_week = 7
units_of_week = "days"


def counting_days(each_week, custome_message):

    print(
        f" the counted days of {each_week} weeks are {each_week * Calculation_of_days_for_week} {units_of_week}")
    print(custome_message)


counting_days(2, "super")
counting_days(3, "awesome")
counting_days(4, "fantastic")
