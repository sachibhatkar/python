"""
    * Class: CS 3A
    * Description: This program takes user input regarding rainfall for each month and stores into a list
    * Later it calculates the average rainfall, the month with the highest rainfall, and the month with the
    * lowest rainfall by accessing the list.
    * Due Date: Aug 2, 2020
    * Name: Sachi Bhatkar
    * Student Id: 20383783
    * File Name: rainfall_statistics.py
"""

"""
* year_months function is used to create a list of 12 months which will later be passed to other functions to create 
* list of rainfall and to calculate which month had  the highest and lowest rainfall 
"""


def year_months():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months


"""
* function which gathers input from user for rainfall for each month and stores into a list
"""


def rain_fall(months):
    input_rain = []
    for i in months:
        print("Enter the rainfall for ", i, ": ", end="")
        user_input = float(input())
        input_rain.append(user_input)
    return input_rain


"""
* total_rain_fall takes the list of inputs as a parameter then calculates the total using the sum method
* it returns that result but rounds it to two places
"""


def total_rain_fall(input_rain_fall):
    total = sum(input_rain_fall)
    return round(total, 2)


"""
* calculate_avg takes the list of inputs as a parameter then calculates the total rainfall by 
* calling the total_rain_fall method then calculates the average and returns  the average rounded to
* 2 decimal places
"""


def calculate_avg(input_rain_fall):
    total = total_rain_fall(input_rain_fall)
    average = total / len(input_rain_fall)
    return round(average, 2)


"""
* get_highest_rain_fall_month function takes two parameters, the list for months and list for inputs 
* it calculates the highest rainfall by using the calculations from before then using that index to pass to the
* month list
"""


def get_highest_rain_fall_month(input_rain_fall, months):
    highest_rain_fall = max(input_rain_fall)
    highest_rain_fall_index = input_rain_fall.index(highest_rain_fall)
    return months[highest_rain_fall_index]


"""
* get_lowest_rain_fall_month function takes two parameters, the list for months and list for inputs 
* it calculates the lowest rainfall by using the calculations from before then using that index to pass to the
* month list
"""


def get_lowest_rain_fall_month(input_rain_fall, months):
    highest_rain_fall = min(input_rain_fall)
    lowest_rain_fall_index = input_rain_fall.index(highest_rain_fall)
    return months[lowest_rain_fall_index]

"""
* print the caluclations regarding the rainfall by passing as a parameter and using print to show on console.
"""


def show_rainfall_statistics(total_rainfall, average_rainfall, highest_rail_fall_month, lowest_rain_fall_month):
    print("\n")
    print("Total rainfall:", total_rainfall)
    print("Average rainfall: ", average_rainfall)
    print("Highest rainfall: ", highest_rail_fall_month)
    print("Lowest rainfall: ", lowest_rain_fall_month)


def main():
    months = year_months()
    input_rain_fall = rain_fall(months)
    total_rainfall = total_rain_fall(input_rain_fall)
    average_rainfall = calculate_avg(input_rain_fall)
    highest_rail_fall_month = get_highest_rain_fall_month(input_rain_fall, months)
    lowest_rain_fall_month = get_lowest_rain_fall_month(input_rain_fall, months)
    show_rainfall_statistics(total_rainfall, average_rainfall, highest_rail_fall_month, lowest_rain_fall_month)


main()
