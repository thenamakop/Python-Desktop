import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with Country code: ")
mobileNo = phonenumber.parse(mobileNo)

#get timezone of a phone no.
print(timezone.time_zones_for_number(mobileNo))

#getting carrier of a phone number
print(carrier,name_for_number(mobileNo, "en"))

#getting region info.
print(geocoder.description_for_number(obileNo, "en"))

#validating a phne number
print("Valid Mobile Numberr :",phonenumbers.is_valid_number(mobileNo))

# checking possibility of a number
print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))


stop()