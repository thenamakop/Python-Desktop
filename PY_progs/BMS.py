#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Maulik
#
# Created:     15-12-2023
# Copyright:   (c) Maulik 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='environ@129',database='n_bank')
cursor=con.cursor()
ctr=0
bank=1
while bank==1:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print("WELCOME T0 NAJJARBATTU BANK ONLINE PORTAL")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Press 1 for Online Banking')
    print('Press 2 for Registering a New Bank Account')
    print('Press 3 for Cancel your Bank Account')
    print('Press 4 for Account Holder Help Services')
    print('Press 5 for Exit')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    choice=int(input("Option : "))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    if choice==1:
        def welcome_message():
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('WELCOME TO NAJJARBATTU BANK')
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        def login():
            while True:
                us=input("Enter your usemame : ")
                p=(input("Entet your password :"))
                print("==============================")
                value=(us,p)
                query="""select * from accounts where usemame=%s and password=-%s """
                cursor.execute(query,value)
                data_login=cursor.fetchall()
                if len(data_login)!=0:
                    globals()['ctr']=1
                    break
                else:
                    print('LOG1N UNSUCCSESSFUL')
                    print("USERNAME OR PASSWORD IS WRONG")
                    print("===================================")
                    return data_login
        def interface():
            welcome_message()
            b=login()
            if globals()['ctr']==1:
                i=b[0][0]
                name=b[0][2]
                print("LOGIN SUCCESSFUL")
                print("====================================")
                c= 1
                while c==1:
                    print('Press 1 for Depositing money')
                    print('Press 2 for Withdrawing money')
                    print('Press 3 for Applying KYC')
                    print('Enter 4 for Loan Request')
                    print('Enter 5 for Insurance Claim')
                    print('Enter 6 for View Full Account Details')
                    print('Press 7 for Checking balance')
                    print('Press 8 for Logging Out')
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    ch=int(input("Enter your option :- "))
                    if ch==1:
                        money_deposit=int(input('Amount To Be Deposited : '))
                        print("=====================================")
                        cursor.execute('update accounts set balance=balance+%s where id=%s',(money_deposit,i))
                        con.commit()
                        q='select balance from amounts where id=%s and usemame=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("Updated Balance: ",x)
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch==2:
                        money_withdrawn=int(input('Amount to be withdrawn : '))
                        print("=====================================")
                        cursor.execute('update accounts set balance=balance-%s where id=%s',(money_withdrawn,i))
                        con.commlt()
                        q='select balance from accounts where id=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("Updated Balance: ",x)
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch==3:
                        q='select kyc from accounts where id=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            condition=x
                        if condition=='false':
                            print('For KYC you need to provide details from one of these Government id')
                            print('Press 1 for Aadhar Card')
                            print('Press 2 for Voter Id Card')
                            print('Press 3 for Pan Card')
                            print('Press 4 for Driving License')
                            print('=====================================')
                            cho-=int(input("Enter your CHOICE : "))
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                            if cho==1:
                                ad=int(input("Aadhar Number : "))
                                cursor.execute('update accounts set kyc="true",govid="aadhar_card",idno=%s where id=%s and username=%s',(ad,i,name))
                                con.commit()
                                print("KYC Done")
                            elif cho==2:
                                vi=int(input("Voter Id Number: "))
                                cursor.execute('update accounts set kyc="true",govid="voter_id",idno=%s where id=%s and usemame=%s',(vi,i,name))
                                con.commit()
                                print("KYC Done")
                            elif cho==3:
                                pc=int(input('Pan Card Number : '))
                                cursor.execute('update accounts set kyc="true",govid=“pan_card",idno=%s where id=%s and usename=%s',(pc,i,name))
                                con.commit()
                                print("KYC Done")
                            elif cho==4:
                                dl=int(input("Driving Licsense Number : "))
                                cursor.execute('update accounts set kyc="true",govid="driving_licesne", idno=%s where id=%s and username=%s',(dl,i,name))
                                con.commit()
                                print("KYC Done")
                            else:
                                print("Wrong Choice")
                        else:
                            print('KYC Already Done')
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch==4:
                        q='select loan from accounts where id=%s and usemame=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            condition=x
                        if condition=='false':
                            print('Choose Type of Loan Requested')
                            print('Press 1 for Housing Loan')
                            print('Press 2 for Personal Loan')
                            print('Press 3 for Educational Loan')
                            print('Press 4 for Agricultural Loan')
                            print('Press 5 for Vehicle Loan')
                            print('Press 6 for Gold Loan')
                            print('================================')
                            cho=int(input("Enter your Choice :- "))
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                            if cho==1:
                                lo=int(input("Enter Amount of Housing Loan Required: "))
                                loi=input("Enter Income Certiﬁcate Number: ")
                                sec=input("Enter Land Document (Security) Number: ")
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)**(yr*12))- 1)
                                print("Najjarbattu Bank charges an Interest of 7% on loans")
                                print("Your Requested loan amount has to be repaid mothly")
                                print("Amount to repay the loan per month: %s ",emi)
                                loa=input("Do you want to continue the loan application? (y/n): ")
                                if loa=='y':
                                    cursor.execute("update accounts set loan= "true" , loan_type="housing", loan_amount=%s, loan_to_be__paid_per_month=%s, loan_duration=%s, income_cert_number=%s, loan_security="landdocument", loan_security_number=%s where id=%s and username=%s",(lo,emi,yr,lol,sec,i,name))
                                    con.commit()
                                    print("Loan Application Approved")
                                    print('======================================')
                                    print('======================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print("======================================")
                                else:
                                    print("Wrong Choice")
                            elif cho==2:
                                lo=int(input("Enter Amount of Personal Loan Required: "))
                                loi=input("Enter Income Certiﬁcate Number: ")
                                secu=input("Enter which Document is been given to the Bank: ")
                                sec=input("Enter Document (Security) Number: ")
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)**(yr*12))-1)
                                print("Najjarbattu Bank charges an Interest of 7% on loans")
                                print("Your Requested loan amount has to be repaid monthly")
                                print("Amount to repay the loan per month: %s",emi)
                                loa=input("Do you want to continue the loan application? (y/n): ")
                                if loa=='y':
                                    cursor.execute('update accounts set loan="true", loan__type="personal", loan_amount=%s, loan_to_be_paid_per_month=%s, loan_duration=%s, income__cert_number=%s, loan_security=%s, loan_security_number=%s where id=%s and usemame=%s',(lo,emi,yr,loi,secu,sec,i,name))
                                    con.commit()
                                    print('====================================')
                                    print("Loan Application Approved")
                                    print('====================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print('====================================')
                                else:
                                    print("Wrong Choice")
                            elif cho==3:
                                lo=int(input("Enter Amount of Educational Loan Required: "))
                                loi=input("Enter School Graduation Certiﬁcate Number: ")
                                secu=input("Enter which Document is been given to the Bank: ")
                                sec=input("Enter Document (Security) Number: ")
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)*(yr*12))-1)
                                print("Najjarbattu Bank Charges an Interest of 7 ","%" ,"on loans")
                                print("Your Requsted loan amount has to be repaid monthly")
                                print("Amount to repay the loan per month: %s",emi)
                                loa=input('Do you want to continue the loan application? (Y/N): ')
                                if loa=='y':
                                    cursor.execute ('update accounts set loan="true", loan_type='educational', loan_amount=%s, loan_to_be_paid__per_month=%s, loan_duration=%s, income_cert_number=%s, loan_security=%s, loan_security_number=%s where id=%s and usename=%s',lo,emi,yr,loi,secu,sec,i,name)
                                    con.oommit()
                                    print('=====================================')
                                    print("Loan Application Approved")
                                    print('=====================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print('=====================================')
                                else:
                                    print("Wrong Choice")
                            elif cho==4:
                                lo=int(input("Enter Amount of Agricultural Loan Required: "))
                                loi=input("Enter Income Certiﬁcate Number: ")
                                secu=input("Enter which Document is been given to the Bank: ")
                                sec=input('Enter Document (Security) Number: ')
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)*(yr*12))-1)
                                print("Najjarbattu Bank charges an lnterest of 7% on loans")
                                print("5Your Requested loan amount has to be repaid monthly")
                                print("Amount to repay the loan per month: %s",emi)
                                loa=input("Do you want to continue the loan application? (y/n): ")
                                if loa=='y':
                                    cursor.execute('update accounts set loan="true", loan_type="agricutural", loan_amount=%s, loan_to_be_paid_per_month=%s, loan_duration=%s, income_cert_number=%s, loan_security=%s, loan_security_number=%s where id=%s and usemame=%s',(lo,emi,yr,loi,secu,sec,i,name))
                                    con.commit()
                                    print("====================================")
                                    print("Loan Application Approved")
                                    print('====================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print('====================================')
                                else:
                                    print("Wrong Choice")
                            elif cho==5:
                                lo=int(input("Enter Amount of Vehide Loan Required: "))
                                loi=input("Enter Income Certificate Number: ")
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)*(yr*12))-1)
                                print("Najjarbattu Bank charges an Interest of 7% on loans")
                                print("Your Requested loan amount has to be repaid monthly")
                                print("Amount to repay the loan per month: %s ",emi)
                                loa=input("Do you want to continue the loan application? (y/n): ")
                                if loa =='y':
                                    cursor.execute('update accounts set loan="true", loan_type="vehicle", loan_amount=%s, loan_to_be_paid_per_month=%s, loan_duration=%s, income_cert_number= %s, loan_security=null, loan_security_number=null where id=%s and usemame=%s',(lo,emi,yr,loi,i,name))
                                    con.commit()
                                    print('====================================')
                                    print("Loan Application Approved")
                                    print('====================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print('====================================')
                                else:
                                        print("Wrong Choice")
                            elif cho==6:
                                lo=int(input("Enter Amount of Gold Loan Required: "))
                                loi=input("Enter income Certificate Number: ")
                                go=input("Enter the Type of Gold Jewel Given at the Bank: ")
                                sec=input("Enter the amount of Gold given to the Bank(in grams): ")
                                yr=int(input("Enter no. of Years you are taking loan for: "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                emi=((lo*0.00583)*(((1.00583)**(yr*12))))/(((1.00583)**(yr*12))-1)
                                print("Najjarbattu Bank diarges an Interest of 7% on loans")
                                print("Your Requested loan amount has to be repaid monthly")
                                print("Amount to repay the loan per month: %s ",emi)
                                loa=input("Do you want to continue the loan application? (y/n): ")
                                if loa=='y':
                                    cursor.execute('update accounts set loan="true", loan_type="gold", loan_amount=%s, loan__to_be_paid__per_month=%s, loan__duration=%s, income_cert_number=%s, loan_security=%s, loan_security_number=%s where id=%s and usename=%s',(lo,emi,yr,loi,go,sec,i,name))
                                    con.commit()
                                    print('====================================')
                                    print("Loan Application Approved")
                                    print('====================================')
                                elif loa=='n':
                                    print("Loan Application Process Aborted")
                                    print('====================================')
                                else:
                                    print("Wrong Choice")
                            else:
                                print('====================================')
                                print("Already Applied For Loan !!")
                                print('===================================')
                    elif ch==5:
                        q='select insurance from accounts where id=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            condition=x
                            if condition=='false':
                                print('Choose Type of Insurance')
                                print('Press 1 for Vehide Insurance')
                                print('Press 2 for Life Insurance')
                                print('Press 3 for Property Insurance')
                                print('Press 4 for Business Insurance')
                                print("===================================")
                                cho=int(input("Enter your choice : "))
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                if cho== 1:
                                    ve=input("Enter Vehicle Manufacturer: ")
                                    ty=input("Enter Vehicle Type: ")
                                    y=int(input("Enter Year of Manufacture: "))
                                    fu=input("Enter Fuel Used: ")
                                    r=input('Enter Vehicle Registration State: ')
                                    m=input('Enter Vehicle Registration Number: ')
                                    if ty=='car':
                                        ins=int(input('Enter Claim Amount for Car to be Insured: '))
                                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                        ina=(((ins/5)*12)-(ins/150))
                                        print("Najjarbattu Bank gives Insurance for cars of: ",ins)
                                        print("Your Requested Insurance Claim Amount has to be paid yearly")
                                        print("Amount to pay for the Insurance Claim Amounet per year: ",ina)
                                        loa=input("Do you want to continue the Insurance Claim application? (y/n): ")
                                        if loa=='y':
                                            cursor.execute("update accounts set insurance="true", insurance_type="vehicle", vehicle_manufacturer=%s, vehicle_model=%s, vehicle_year=%s, vehicle_fuel=%s, vehicle_reg_state=%s, vehicle_reg_no=%s, insuarnce_amount=%s, insurance_to_be_paid_per_year=%s where id=%s and username=%s".(ve,ty,y,fu,r,m,ins,ina,i,name))
                                            con.commit()
                                            print('=====================================')
                                            print("Insurance Claim Taken")
                                            print('=====================================')
                                        else:
                                            print('Insurance Claim Aborted')
                                            print('=====================================')
                                    elif ty=='bike':
                                        ins=int(input(" Enter Claim Amount for Bike to be Insured: "))
                                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                        ina=((ins/5)/15)
                                        print("Najjarbattu Bank gives Insurance for bikees of: ",ins)
                                        print("Your Requested Insurance claim Amount has to be Paid Yearly")
                                        print("Amount to pay the for Insurance Claim Amount per year: ",ina)
                                        loa=input('Do you want to continue the Insurance Claim application? (y/n): ')
                                        if loa =='y':
                                            cursor.execute('update accounts set insurance="true", insurance_type="vehicle", vehicle_manufacturer=%s, vehicle_model=%s, vehicle__year=%s, vehide_fuel=%s,vehicle_reg__state=%s,vehicle_reg_no=%s,insurance_amount=%s, insurance_to_be_paid_per_year=%s where id=%s and username=%s',(ve,ty,y,fu,r,rn,ins,ina,l,name))
                                            con.commit()
                                            print=('=======================================')
                                            print('Insurance Claim Taken')
                                            print("========================================")
                                        else:
                                            print("Insurance Claim Aborted")
                                            print('========================================')
                                elif cho==2:
                                    mc=input("Enter Medical Certiﬁcate Number: ")
                                    bc=input("Enter Birth Certiﬁcate Number: ")
                                    ins=int(input("Enter Claim Amount to be Insured: "))
                                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                    ina=(ins/12)-(ins/20)
                                    print("Bank of Grlngotts gives Life Insurance of: ",ins)
                                    print("Your Requested Insurance Claim Amount has to be paid Yearly")
                                    print("Amount to pay the for Insurance Claim Amount per year: ",ina)
                                    loa=input("Do you want to continue the Insurance Claim application? (y/n): ")
                                    if loa=='y':
                                        cursor.execute('update accounts set insurance="true", insurance_type="life", medical_cert_no=%s, birth_cert__no=%s, insurance__amount=%s, insurance_to_be_paid_per_year=%s where id=%s and username=%s',(mc,bc,ins,ina,i,name))
                                        con.commit()
                                        print("=====================================")
                                        print("Insurance Claim Taken")
                                        print('=====================================')
                                    else:
                                        print('Insurance Claim Aborted')
                                        print('=====================================')
                                elif cho==3:
                                    dc=input("Enter Property Dowment Number: ")
                                    ﬁ=input("Enter FIR Number (FOR THEFT OR LOSS): ")
                                    ins=int(input("Enter Claim Amount to be Insured: "))
                                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                    ina =(ins/12)/7
                                    print("Najjarbattu Bank gives Property Insurance of: ",ins)
                                    print("Your Requested Insurance Claim Amount has to be paid yearly")
                                    print("Amount to pay for the Insurance Claim Amount per year: ",ina)
                                    loa=input("Do you want no continue the Insurance Claim application? (y/n): ")
                                    if loa=='y':
                                        cursor.execute('update accounts set insurance="true", insurance_type="property", property_no=%s, ﬁr_no=%s, insurance_amount=%s, insurance_to_be_paid_per_year=%s where id=%s and username=%s',(dc,fi,ins,ina,l,name))
                                        con.commit()
                                        print("=====================================")
                                        print("Insurance Claim Taken")
                                        print('=====================================')
                                    else:
                                        print("Insurance Claim Aborted")
                                        print('=====================================')
                                elif cho==4:
                                    em=input("Enter Employment Building Name: ")
                                    a=input("Enter Cause of Claim: ")
                                    de=input("Enter Medical/Death Certificate Number: ")
                                    ins=int(input("Enter Claim Amount to be Insured: "))
                                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                    ina=(ins/12)/7
                                    print("Najjarbattu Bank gives Business Liability Insurance of: ", ins)
                                    print("Your Requested lnsurance Claim Amount has to be paid yearly")
                                    print('Amount to pay for the Insurance Claim Amount per year: ',ina)
                                    loa-input("Do you want to continue the Insurance Claim application? (y/n): ")
                                    if loa=='y':
                                        cursor.execute('update accounts set insurance="True", insurance_type='buisness', building_name=%s, cause_of_claim=%s, med_death_cert_no=%s, insurarce_amount=%s, insurance_to_be_paid_per_year=%s where id=%s and username=%s', (em,ca,de,ins,ina,i,name))
                                        con.commit()
                                        print('========================================')
                                        print("Insurance Claim Taken")
                                        print("========================================")
                                    else:
                                        print("Insurance Claim Aborted")
                                        print('========================================')
                                else:
                                        print("========================================")
                                        print("Insurance Already Claimed !!")
                                        print("=========================================")
                    elif ch==6:
                        q='select * from amounts where id=%s and usemame=%s'
                        cursor.execute(q.(i.name))
                        a=cursor.fetchall()
                        for x in a:
                            print("Account Number: ",x[0])
                            print("------------------------------")
                            print("Account Holder's Name: ",x[1])
                            print('----—-------------------------')
                            print("Acoount Holder's Usename': ",x[2])
                            print('----—-------------------------')
                            print("Account Balance: ",x[4])
                            print('----—-------------------------')
                            print("Acoount Holder's Age: ",x[5])
                            print('----—-------------------------')
                            print("Account Holder's Gender: ",x[6])
                            print('----—-------------------------')
                            print("Account Holder's Number: ",x[7])
                            print('----—-------------------------')
                            print("Accoount Holder's street address: ",x[8])
                            print('----—-------------------------')
                            print("Account Holder's dstrict address: ",x[9])
                            print('----—-------------------------')
                            print("Account Holder's pin code address: ",x[10])
                            print('----—-------------------------')
                            print("Account Holder's state: ",x[11])
                            print('----—-------------------------')
                            print("Account Holder's country: ",x[12])
                            print('----—-------------------------')
                            print("KYC: ",x[13])
                            print('----—-------------------------')
                            print("Account Holder's Nominee: ",x[14])
                            print("------------------------------")
                            print("Account Holder's Government id For KYC: ",x[15])
                            print('------------------------------')
                            print("Account Holder's Government id Number For KYC: ",x[16])
                            print("------------------------------")
                            print("LOAN= ",x[17])
                            print("------------------------------")
                            if x[17]=='true':
                                print("Acoount Holder's Loan Type: ",x[18])
                                print("------------------------------")
                                print("Account Holder's Loan Amount: ",x[19])
                                print("------------------------------")
                                print("Account Holder's Loan Amount to be Paid per Month: ",x[20])
                                print("------------------------------")
                                print("Account Holder's Loan Duration: ",x[21])
                                print("------------------------------")
                                print("Acoount Holder's Income Certiﬁcate Number: ",x[22])
                                print("------------------------------")
                                print("Aooount Holder's Loan Security: ",x[23])
                                print("------------------------------")
                                print("Account Holder's Loan Security Number/Weight: ",x[24])
                                print("------------------------------")
                            print("INSURANCE: ",x[25])
                            print("------------------------------")
                            if x[25]=='true':
                                print("Account Holder's Insurance Type: ",x[26])
                                print("------------------------------")
                                if x[26]=='vehicle':
                                    print("Acoount Holder's Insurance Amount: ",x[27])
                                    print("------------------------------")
                                    print("Account Holder's insurance Amount to be Paid per Year: ",x[28])
                                    print("------------------------------")
                                    print("Account Holder's Insured Vehicle Vehicle Manufacturer: ",x[29])
                                    print("------------------------------")
                                    print("Account Holder's Insured Vehicle Model: ",x[30])
                                    print("------------------------------")
                                    print("Account Holder's Insured vehicle Model Year: ",x[31])
                                    print("------------------------------")
                                    print("Account Holder's Insured Vehicle Fuel Type: ",x[32])
                                    print("------------------------------")
                                    print("Account Holder's Insured Vehicle Registered State: ",x[33])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Vehicle Registered Number: ",x[34])
                                    print("------------------------------")
                                elif x[26]=='life':
                                    print("Account Holder's Insurance Amount: ",x[27])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Amount to be Paid per Year: ",x[28])
                                    print("------------------------------")
                                    print("Account Holder's Medical Certiﬁcate Number: ",x[35])
                                    print("------------------------------")
                                    print("Account Holder's Birth Certiﬁcate Number: ",x[36])
                                    print("------------------------------")
                                elif x[26]=='property':
                                    print("Account Holder's Insurance Amount: ",x[27])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Amount to be Paid per Year: ",x[28])
                                    print("------------------------------")
                                    print("Account Holder's Insured Property Number: ",x[37])
                                    print("------------------------------")
                                    print("Account Holder's FIR Number (Incase of Theft or Damage to Property): ",x[38])
                                    print("------------------------------")
                                elif x[26]=='business':
                                    print("Account Holder's Insurance Amount: ",x[27])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Amount to be Paid per Year:",x[28])
                                    print("------------------------------")
                                    print("Account Holder's Insured Building Name: ",x[39])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Amount Claiming Cause: ",x[40])
                                    print("------------------------------")
                                    print("Account Holder's Insurance Amount Claiming Medical/Death Certiﬁcate Number: ",x[41])
                    elif ch==7:
                        q='select balance from accounts where id=%s and usemame=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("Balance :- ",x)
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch==8:
                        c=0
                    else:
                        print("Wrong Option ")
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        interface()
    elif choice==2:
        print("FILL THESE DETAILS TO CREATE YOUR ACCOUNT:- ")
        idea=random.randint(1,100)
        name=input("Enter your name : ")
        username=input('Enter your username : ')
        pas=input('Enter your password : ')
        balance=ﬂoat(input('Enter your balance : '))
        age=int(input('Enter your age : '))
        gender=input('Enter your gender (M/F) : ')
        mob=int(input('Enter Mobile no. : '))
        street=input('Enter your street name: ')
        district=input('Enter your District: ')
        pincode=int(input('Enter your Pincode: '))
        state=input('Enter State: ')
        country=input('Enter your Country: ')
        nominee=input("Enter Nominee Name (lncase after Death the Account Credentials have to be handed Over): ")
        print('====================================================')
        kyc='false'
        loan='false'
        insurance='false'
        query='insert into accounts values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,%s,null,null,null,null,null,null,null,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);'
        value=(idea,name,username,pas,balance,age,gender,mob,street,district,pincode,state,country,kyc,nominee,loan,insurance)
        cursor.execute(query,value)
        con.commit()
        print('====================================================')
        print('Bank Account Successfully Created')
    elif choice==3:
        us=input("Enter your username :- ")
        p=(input("Enter Your Password :-"))
        print('====================================================')
        value=(us,p)
        query="select * from accounts where usemame=%s and password=%s "
        cursor.execute(query,value)
        data_login=cursor.fetchall()
        cursor.execute('delete from accounts where id=%s and usemame%s',(data_login[0][0],data_login[0][2]))
        con.commit()
        print('====================================================')
        print('Bank Account Successfully Closed')
    elif choice==4:
        print('TOLL FREE NO - 9079209924')
        print('====================================================')
    elif choice==5:
        bank=0
    else:
        print("Wrong Option")
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#END OF SOURCE CODE#
