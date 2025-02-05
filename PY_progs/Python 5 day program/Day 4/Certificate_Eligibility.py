#Certificate_Eligibilit_Program
#made by : Maulik Gupta @thenamakop
#
def main():
    print("Welcome to the Certificate Eligibility Checking Program")
    attendance = int(input("Enter your attendance through the workshop: Enter [1] if you have joined every day and enter [2] if you had a day or more's absence"))
    certificate_eligibility_check(attendance)

def certificate_eligibility_check(attendance):
    if attendance == 1:
        print("You have joined every day")
        print("Now, Please answer this questionaire:")
        ques1 = int(input("Enter [1], if you have submitted every day's assignment."))
        if ques1 == 1:
            ques2 = int(input("Now, Enter [1] if you were present on-time in each and every live class. Enter [2] if you werent present even one a single day."))
            if ques2 == 1:
                ques3 = int(input("Now, Enter [1], if your camera was on in the classes. Enter [2] if your camera wasn't."))
                if ques3 == 1:
                    print("Congratulations!!! You are eligible for the certificate.")
                elif ques3 == 2:
                    print("You didn't have your camera on during the classes.")
                    print("Sorry, You are not eligible for the certificate")
                else:
                    print("You have entered an invalid input.")
                    print("Please try again.")
            
            elif ques2 == 2:
                print("You weren't present on-time in one or more classes.")
                print("Sorry, You are not eligible for the certificate.")
            else:
                print("You have entered an invalid input.")
                print("Please try again.")
        elif ques1 == 2:
            print("You have not submitted every day's assignment.")
            print("Sorry, You are not eligible for the certificate.")
        else:
            print("You have entered an invalid input.")
            print("Please try again.")            
                
    elif attendance == 2:
        print("You have had a day or more's absence.")
        print("Sorry, You are not eligible for the certificate.")
    else:
        print("You have entered an invalid input.")
        print("Please try again.")
        
if __name__ == "__main__":
    main()
#end of source code