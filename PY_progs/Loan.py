'''Task: Write a program to determine if an applicant is eligible for a loan. The
eligibility criteria are based on age, annual income, and employment type
(salaried or self-employed).
● Age must be between 22 and 60.
● Minimum annual income of $30,000.
● Salaried applicants are eligible with the minimum criteria, but
self-employed applicants need a minimum annual income of $40,000.
Input Format: The program should ask for the applicant's age, annual income,
and employment type.
Output Format: The program should print "Eligible for loan" or "Not eligible
for loan".
Example:
● Input: Age = 30, Income = 35000, Employment Type = Salaried
● Output: Eligible for loan'''

def Loan_Eligibility(age, income, status):
    if age >= 22 and age <= 60 and income >= 30000 and status == "salaried":
        print("Eligible for loan")
    elif age >= 22 and age <= 60 and income >= 40000 and status == "self-employed":
        print("Eligible for loan")
    else:
        print("Not eligible for loan")



#main
print("Loan Eligibility Program: ")
age = int(input("Please enter Your age: "))
income = int(input("Please enter your income : "))
status = input("Please enter your employment status : Enter salaried if you are salaried and self-employed if you are self-employed: ")
Loan_Eligibility(age, income , status)