def Insert_Into_List():
    x=[]
    items = int(input("How Many Items You want to add in the list: "))
    for i in range(items):
        ins=int(input("Please Insert a value into the list: "))
        x.append(ins)
    
    def printout():
        choice=input("Do You want printout of the list(Type 'yes' or 'no'): ")
        if choice == 'yes':
            print(x)
        elif choice == 'no':
            print("Thank You for using this program.")
        else:
            print("Wrong Input. Please try again")
            printout()
    printout()
        

if __name__ == '__main__':
    Insert_Into_List()
