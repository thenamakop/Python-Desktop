# Currency Converter: Write a Python code that converts US dollars to Euros.
# The program should ask the user to input the amount in US dollars and
# use a conversion rate of 1 USD = 0.85 Euros to convert and display the amount in Euros.
def Converter(USD):
    Euros = USD * 0.85
    print("The amount in Euros is: ", Euros)

def main():
    print("Welcome to the Currency Converter")
    USD = float(input("Enter the amount in US dollars which you want in Euros: "))
    Converter(USD)
    
main()