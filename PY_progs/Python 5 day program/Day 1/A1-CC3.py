#. Implement a Python application that requests the user's name and age.
# The program should then calculate and inform the user of the year they will turn 100 years old.
def calculate_year_to_100(age):
    from datetime import date
    current_year = date.today().year
    Year_to_100 = current_year + (100 - age)
    return Year_to_100
#main
name = input("What is your name?: ")
age = int(input("What is your age? : "))
year_to_100 = calculate_year_to_100(age)
print(name,", You will turn 100 years old in the year" , year_to_100,".")