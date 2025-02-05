pi = 3.14
r = float(input("Please enter the radius of circle(in cm): ")) # radius
if r <= 0:
    print("The radius should be greater than 0")
area = (pi * r**2)
print("The area of the circe is: ", area, "cms. squared")
