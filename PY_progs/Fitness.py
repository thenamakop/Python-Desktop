'''Question 1: Fitness Tracker (5M)
Scenario: You're developing a fitness tracker app that recommends daily activity levels
based on steps taken.
3
]\
Problem: Write a program that gives recommendations based on the number of steps
input:
● Below 5,000 steps: "Try to be more active."
● Between 5,000 and 10,000 steps: "Good job on staying active!"
● Above 10,000 steps: "Great work! You're leading a very active lifestyle."
Example Input-Output:
● Input: 7000
● Output: "Good job on staying active!"
'''

def Fitness(steps):
    if steps < 5000:
        print("Try to be more Active.")
    elif steps >= 5000 and steps <= 10000 :
        print("Great Job on being Active!")
    elif steps > 10000 :
        print("Great work! You're leading a very active lifestyle.")

#main
print("Welcome to the fitness tracker program:- ")
steps = int(input("Please enter your today's step count: "))

Fitness(steps)