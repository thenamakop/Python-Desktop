# Daily Steps Tracker: Write a Python program that asks the user to enter the number of steps they walked
# each day for a week. After entering seven numbers, the program should calculate and display the total number of steps 
# walked in the week
def Steps_Tracker(D1, D2, D3, D4, D5, D6, D7):
    steps = D1 + D2 + D3 + D4 + D5 + D6 + D7
    print("Your weekly step count is : ", steps)
    if steps < 60000:
        print("Your Weekly Step Count is lower than average, I suggest you should walk more for your proper health.")
    
#main():
print("********************Welcome to the StepTracker*************************")
print("Please enter the number of steps you walked each day as follows:- ")
D1 = int(input("Enter the number of steps you walked on Day 1: "))
D2 = int(input("Enter the number of steps you walked on Day 2: "))
D3 = int(input("Enter the number of steps you walked on Day 3: "))
D4 = int(input("Enter the number of steps you walked on Day 4: "))
D5 = int(input("Enter the number of steps you walked on Day 5: "))
D6 = int(input("Enter the number of steps you walked on Day 6: "))
D7 = int(input("Enter the number of steps you walked on Day 7: "))

Steps_Tracker(D1, D2, D3, D4, D5, D6, D7)