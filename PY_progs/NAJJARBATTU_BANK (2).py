import random
import mysql.connector as pymysql
con=pymysql.oonnect(host='localhost‘,user='root‘,password='environ@129‘,database=‘BANK')
cursor=con.cursor()
ctr=0
bank=1
while bank==1:
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print("WELCOME T0 BANK OF GRINGOTTS ONLINE PORTAL")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('Press 1 for Online Banking‘)
print('Press 2 for Registering a New Bank Account’)
print('Press 3 for Cancel your Bank Account‘)
print('Press 4 for Account Holder Help Services‘)
print('Press 5 for Exit‘)
print(’>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
d1oice=int(input("Option : "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
if choice==1:
def welcome_mssage():
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('WELCOME TO BANK OF GRINGOTTS')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>‘)
def login():
while True:
us=input("Enter your usemame : ")



p=(input("Entet your password :'))
pf‘i|1t('=====::zz:::====:===::8=========::a:==')
value=(us,p)
query="‘select ' from accounts where usemame=%s and
password=-%s """
cursor.exealte(query,value)
data_|ogin=cursor.fetchall()
if len(data_login)!=0:
9k>baIs()[°ch’]=1
break
else:
print('LOG1N UNSUCCSESSFUL‘)
print("USERNAME OR PASSWORD IS WRONG‘)
pm:('===========----===================='>
retum data__login
def im:erfaoe():
weloome_m&age()
b=login()
if globals()['ctr‘]==1:
i=b[0][0]
name=b[0][2]
print("LOGIN SUCCESSFUL”)
wnw===================================='>
c= 1
while c==1:
print('Press 1 for Depositing money’)
print('Press 2 for Withdrawing money‘)
print('Press 3 for Applying KYC‘)
print('Enter 4 for Loan Request‘)
print(‘Enter 5 for Insurance Claim‘)
print('Enter 6 for Vuew Full Account Details’)



print(‘Press 7 for Checking balance‘)
print('Press 8 for Logging 011')
prlnt('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>‘)
ch=int(input("Enter your option 2- "))
if d1= I 1:
money_deposlt=int(input('Amount no be deposited : '))
mmdw==============-=======-==============7
cursor.en<ecute('update accounts set balance=balance+%s where
id=%5'.(m0ﬂeY_dep0$it.i))
con.commit()
q='select balance from amounts where id=%s and usemame=%s‘
cursor.exeu:te(q,(i,name))
a=cursor.fetd1all()
a=a[0]
for x in a:
print("Updated Balance: ",x)
ptint('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>‘)
elif d1= =2:
m0ney_withdrawn=int(input(‘Am0unt to be withdrawn :- '))
wmd@==============-====================w
cursor.a<eo.:te('update accounts set balance=balance-%s where
id=%s',(money_vw‘thdrawn,i))
con.commlt()
q='select balance from accounts where id=%s and username=%s’
cursor.exewte(q,(l,name))
a=cursor.fetcha||()
a=a[0]
for x in a:
print("Updated Balance: ",x)
print(‘>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ellf ch= =3:
q='select kyc from accounts where id=%s and username=%s'



cursor.execute(q,(i,name))
a=cursor.fetchall()
a=a[0]
for x in a:
condition=x
if condition-===‘false':
print('For KYC you need to provide details from one ofthese
Qwemmeﬂl id‘)
print('Press 1 for Aadhar Card‘)
prInt(‘Pre$$ 2 for Voter Id Card’)
print('Press 3 for Pan Card’)
print('Prss 4 for Driving Ucense‘)
mmx'=====================-=-=============->
cho-=int(input("Enter your C|'I0iCE :- "))
pdnt('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
if cho==1:
ad=int(input("Aadhar Number : "))
cursor.execute('update accounts set
kyc=“true",govid="aadhar_card",idno=%s where id=%s and
username=%s’,(ad,i,name))
con.commit()
prInt("KYC Done")
elif cho==2:
vi=int(input("Voter Id Number: "))
cursor.execute('update accounts set
kyc-"true",govid='voter_id',idno=%s where ld==%s and usemame=%s',(vi,i,name))
oon.commit()
print('KYC Done")
elif d\o==3:
pc=int(input("Pan Card Number : '))
a:rsor.execute(‘updaue accounts set
kyc="true",govid=“pan_card",idno=%s where id=%s and
usemame==°/os',(pc,i,name))



con.oommit()
vfiﬂt(“KY¢ Owe‘)
elif cho==4:
dI=int(inputa('DrMng Uoense Number : "))
cursor.execute('update amounts set
kyc='true',govid='drivIng_l6oenoe',idno=%s where id-%s and
username-=%s',(dl,i,name))
oon.oommit()
P'iM("KY€ Owe’)
eisez
0'i"t('W'0ﬂ9 ¢h°‘0B')
else:
print(’KYC Already Done’)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
elif ch-=4:
q=-‘select loan from acooums where id-%s and usemame-%s‘
¢ws0r.e><ewre(q.(i.name))
a=cursor.fetd\all()
a=a[0]
for x in a:
condition-x
ifconditi0n==‘false':
print('Choose Type of Loan Requested’)
priﬂt('Pms$ 1 for Housing Loan’)
print('Press 2 for Personal Loan‘)
print('Pr& 3 for Edutﬁonal man‘)
print(‘Press 4 for Agﬂctltural Loan’)
p1int('Pr& S for Vehide Loan‘)
print('Press 6 for Gold Loan’)
wnw------=---=---=--=------H----------'>
dro-int(input('Enter your dwoioe :- "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')



if cho==1:
lo-int(lnput("Ent:er Amount of Housing Loan Required: "))
lol=input('Enter Income Certiﬁcate Number: ")
sec=input("Enter Lard Document (Security) Number: ")
yr=int(input("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>‘)
emi=((lo'0.00583)*(((1 .oosa3)' "(yr"‘12))))I(((1.00S83)**(yr"12))- 1)
mvnfﬂv")
(Y/n)= ")
print("Bank of Grlngotts dwarges an Interest of 7% on loans‘)
print("Your Requested loan amount has to be repaid
print(‘Amount to repay the loan per month: %s",eml)
loa=input("Do you want to continue the loan application?
if |oa= =‘y‘:
cursor.exeune('update accounts set
loan="true",loan_type="nouQng",loan_amount=%s,loan_to_be__pald_per_mont.h=
%s,loan_dural5on=%s,inoome_oert__number=%s,loan_security="landdooument",loa
n_security__number=%s where ld=%s and usemame=%s’,(lo,emi,yr,Iol,sec,i,name))
con.oornmit()
print("l.oan Application Approved’)
pfiﬂ[('======:nas=====:===:|::z:|========a:=:')
pf|f|t('==========:::B::==========:=:=========')
elif |oa=='n':
prinl:("L0an Application Process Aborted‘)
pfintcs=3:=====::==:=a:==========:a::==::===')
Bank: -)
else:
print("Wrong Choice’)
elif cno==2:
lo=int(input("Enter Amount of Personal Loan Required: "))
loi=input("Enter Income Certiﬁcate Number: ")
secu=input("Enter whid1 Document ls been given to the



SeC=input("Enter Document (Security) Number: ")
yr=int(input("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
emi=((lo‘0.00583)“(((1.00583)*'(yr"12))))l(((1.00583)**(yr*12))-1)
print("Bank of Gringoﬂs d1arges an Interest of 7% on loans")
print("Your Requested loan amount has to be repaid
m<>ﬂﬂ1lY")
print("Amount to repay the loan per month: %s',emi)
loa=input("Do you want to continue the loan application?
(Y/")1 ")
if loa=='y':
cursor.execute('update accounts set
loan="true",loan__type="personal“,loan_amount=%s,loan_to_be_paid_per_month=
%s,loan_duration=°/us,income__cert_numbe'=%s,loan_security=%s,loan_semrity_n
umber=%s where id=%s and usemame=%s‘,(lo,emi,yr,loi,secu,sec,i,name))
con.commit()
pmr('====================================')
print('Loan Application Approved")
print('====================================')
elifloa=='n':
print("Loan Application Rocess Aborted")
nrint(‘====================================')
else:
print("Wrong Choice")
elif d\o==3:
lo=int(input("Enter Amount of Educational Loan Required: "))
loi=input("Enter Sd\ool Graduation Certiﬁcate Number: ")
secu=input("Enter whid1 Document is been given to the
Bank: ")
sec=input("Enter Document (Security) Number: ")
yr=int(input("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
emi=((lo"0.00S83)"(((1.00S83)”(yr*12))))/(((1.00S83)“(yr'12))-1)



print("8ank of Gringotts C|"l3fQ2S an Interest of 7% on loans")
prlnt("Your Requsted loan amount has to be repaid
monthly")
print("Amount to repay the loan per month: %s“,eml)
|qa=input('Do you want to oontlnue the loan application?
(Y/")1 ')
if loa= ='y':
cursor.execute('updatle aooounts set
loan="true",loan_type='educational',loan_amount=%s,loan_to_be_paid__oer_m0nth
=%$,loan_duration=%s,inoome_oert_number=%s,loan_securlty=%s,loan_security_
number=%s where id=%s and usemame=%s',(lo,eml,yr,loi,secu,Se€,i.I\8m6))
con.oommit()
pIint('=======================“"=========‘"")
print("Loan Application Approved‘)
print('====================-================')
ellf loa=='n':
print("Loan Application Process Aborted")
print('==============================="=====')
else:
print("Wrong Choice")
elif cho==4:
lo=lnt(input("Enter Amount of Agricultural Loan Required: "))
lol=input("Enter Income Certiﬁcate Number: ")
secu=lnput("Enter which Document ls been given to the
Bank: ')
sec=input:(‘Enter Document (Security) Number: ")
yr=int(input("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')emi=((|q*0_0(]533)'(
((1-°°583)**(Yr"1Z))))!(((1.00S83)"(yr‘12))-1)
print("8ank of Gringotis dmarges an lnteest of 7% on loans‘)
print('Your Requested loan amount has to be repaid
monthly")
print("Amount to repay the loan per month: %s",emi)



loa=input("Do you want to continue the loan application?
(Y/")1 ")
if loa==‘y':
cursor.execute('update accounts set
loan="true",loan_type="agricull11ral",loan_amount=%s,loan_to_be_paid_per_month
=%s,loan_duration=%s,income_0ert_number=%s,loan_security=%s,loan_security__
number=°/as where id=%s and usemame=%s',(lo,emi,yr,l0i,secu,sec,i,name))
oon.oommit()
prinv<'====================================')
print("Loan Application Approved")
r>Iint('===================================')
elif |oa==‘n':
print("Loan Application Procas Aborted“)
prinr<'====================================')
else:
print("Wrong Choice")
elif cho==5:
lo=int(input("Enter Amount of Vehide Loan Required: "))
loi=input("Enter Income Certiﬁcate Number: ")
yr=int(input("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
emi=((lo*0.00S83)*(((1.00S83)**(yr“ 12))))/(((1.00S83)"(yr"12))-1)
print("Bank of Gringotis charges an Interest of 7% on loans")
print("Your Requested loan amount has to be repaid
monthly")
print("Amount to repay the loan per month: %s",emi)
loa=input("Do you want to continue the loan application?
(Y/n)= ")
if loa= ='y':
cursor.execute('update accounts set
loan="true“,loan_type="vehicle",loan_amount=%s,loan_to_be_paid_per_month=%
s,loan_duration=%s,income_oert_number= %s,loan_security=null,Ioan_security_nu
mber=null where id=%s and usemame=%s',(lo,emi,yr,loi,i,name))
0on.commit()



prinr<'===================================='>
print("Loan Application Approved")
prinr<'===================================='>
ellf loa==‘n‘:
print("Loan Application Process Aborted")
prinr<'====================================')
else:
print("Wrong Choice")
elif cho==6:
lo=int(input("Enter Amount of Gold Loan Required: "))
loi=input("Enter income Cerﬁﬁcate Number: ")
go=input("Enter the Type of Gold Jewel Given at the Bank: ")
sec=input("Enter the amount of Gold given to the Bank(in
grams): ”)
yr=inqinput("Enter no. of Years you are taking loan for: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
emi=((lo"0.00583)"(((1.00583)"(yr"12))))/(((1.00583)"(yr'12))-1)
print("Bank of Gringotts diarges an Interest of 7% on loans")
print("Your Requested loan amount has to be repaid
monthly")
print("Amount to repay the loan per month: %s",emi)
loa=lnput("Do you want to continue the loan application?
(v/n): ")
if loa=='y‘:
cursor.execute('update accounts set
loan=“true",loan_type="gold",Ioan_amount=%s,loan__to_be_paid__per_month=%s,lo
an__duration=%s,income_oert_number=%s,loan_security=%s,loan_security_number
=%s where id=%s and usemame=%s',(lo,emi,yr,loi,go,sec,i,name))
con.commit()
pmw===================================='>
print("Loan Application Approved")
pnnr<'===================================='>
elif loa=='n‘:



print("Loan Application Process Aborted“)
pm:<'===================================='>
else:
print("Wrong Choice")
else:
prinr('===================================='>
print("Already Loan Applied !!")
wmﬂe===================================)
elif d1==5:
q='select insurance from accounts where id=%s and
usemame=%s'
curs0r.execute(q,(i,name))
a=cursor.fetchall()
a=a[0]
for x in a:
condition=x
if condition==‘false':
print('Choose Type of Insurance‘)
print('Press 1 for Vehide Insurance‘)
print('Press 2 for Life Insurance‘)
print('Press 3 for Property Insurance‘)
print(‘Press 4 for Business Insurance’)
mmﬂe===================================)
cho=6nt(input("Enter your choice :- "))
print(‘>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
if cho== 1:
ve=input("Enter Vehicle Manufacturer: ")
ty=input("Enter Vehicle Type: ")
y=int(input("Enter Year of Manufacture: "))
fu=input(“Enter Fuel Used: ")



r=input('Enter Vehide Registration State: -)
m=lnput('Enter Vehide Registration Number. ')
if ty=='car’:
_» ins=int(input('Enter Claim Amount for Car m be Insured:
ymﬂ$>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>§
iﬂ6=((ir\$/S)l12)-(inSl150)
mmK1hNu#Gﬁmpns¢w5hwwmxeﬁxamsdéZmQ
mmwwmxkamennhswmweO&mAnnunmuuMm
Paid veaﬂf)
wmM1mmumnomwUnﬁxhwmaxeO&mAmuuKpr
W3" '.ina)
ka=mpxCDowmuamnoammmeﬁnhummmeﬂmm
annlimﬁon? (yin): ')
KkB==YE
cmumeeammwmrammmmsn
mwnmm=$m€ﬂswmxgjwn=Wdmh2wmkkJmmmHmma=%mwmkbJmﬁd
=%&W$kEJ@N=%&W$HQﬂﬂ=%&WﬁHQﬂjB@=%&W$HQﬂJD=%&i
mmmnmjmnwm=%wmumam2JnJnJwHJxLyau=%sumaeH=%smM
usemame=%s‘,(ve.tv.v.fu.r,m.ins,ina.i.name))
annmwmﬂ)
WmK%===================================7
mmq1mmmmChmfhMm?
pmw===================================='>
dm:
printflrsuranoe Oaim Aborted")
mﬂK'=======::==::====:====:.:===::===========')
dWW=€HHﬁ
hs=mdmmﬂ1muxGmmAnnutﬁxﬂweunnlmmm
"))
mhK$>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>)
iﬂ8=((iI1$/5)/15)
wmwﬂmmoﬂkhgmgwshswmtekrUhsoh2mQ



prlnt('YourRequestedInsurance(JaimAmounthastobe
Paid YwlY")
print(“Amount to pay the for Insxrance Claim Amount per
vein “,iﬂa)
loa=input('Do you want to continue the Insurance Claim
apnliwﬁm? (Y/n)= ')
if loa= ='y':
cursor.execut:e('update accounts set
insurance="true",irsuranoe_type="vehicle",vehlcle_manufacturer=%s,vehide_model
=%s,vehide__year=%s,vehide_fuel=%s,vehlde_reg__state=%s,vehide_reg_no=%s,i
nsuranoe_amount=%s,insurance__to_be_paid_per_year=%s where id=%s and
usemame=%s',(ve,ty,y,fu,r,rn,ins,ina,l,name))
oon.commlt()
mn=('=-==-=-==-=--=--=-=====================w
prlnt("Insuranoe Claim Taken‘)
m~w-==-=-==--=--==-===================='>
else:
prInt("Insuranoe Claim Aborted‘)
wm('===----==--========================='>
ellf cho===2:
mc-input("Enter Medical Certiﬁcate Number: ")
bc-lnput("Enter Birth Certiﬁcate Number: ")
ins-int(input("Enter Claim Amount to be Insured: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ina=(lns/12)-(ins/20)
print("Bank of Grlngotts gives Life Insurance of: ",ins)
print("Your Requested Insurance Claim Amount has to be paid
Yearly")
print("Amount in pay the for Insurance Claim Amount per
year: ',ina)
loa=input("Do you want to continue the Insurance Claim
application? (yin): ")
if loa=='y':
cursor.execute(‘update accounts set
insurance="true',insuranoe_type="life",medical_oert_no=%s,birth_cert__no=%s,insu



ranoe__amount=%s,insurance_to_be_paid_per_year=%s where id=%s and
usemame=%s',(mc,bc,ins,ina,i,name))
con.oommit()
mmu@===================================v
print("Insurance Oaim Taken")
print('====================================')
else:
print("Insuranoe Claim Aborted‘)
mmu@===================================v
elif cho==3:
dc=input(“Enter Property Dowment Number: “)
ﬁ=input("Enter FIR Number (FOR THEFT OR LOSS): ”)
ins=int(input("Enter Claim Amount to be Insured: "))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ina =(ins/12)/7
print("Bank of Gringotts gives Property Insurance of: ",ins)
print("Your Requested Insurance Claim Amount has to be paid
veaﬂv')
prinu("Amount no pay the for Insurance Claim Amount per
year: ",ina)
loa=input("Do you want no continue the Insurance Claim
application? (y/n): ")
if loa=='y':
cursor.execute(‘update accounts set
insuranoe="true",insurance_type="property",property_no=%s,ﬁr_no=%s,insuranoe
_amount=%s,insuran0e_ln__be_paid_per_year=%s where id=%s and
usemame=%s',(dc,fi,ins,ina,l,name))
oon.oommit()
wmd%===================================3
print("Insurance Oaim Taken")
wmu==============-=====================v
else:
print("Insurance Gaim Aborted‘)



wI~m'--------==-=---------------------==-'>
elif cho-=4:
em-input("Enter Employment Building Name: ")
a=input("Enter Cause of Claim: ")
de-input(“Enter Medical/Death Cﬁtiﬁmte Number: ")
in$Iint(input("En!!!I' Claim Amount to be Insured: “))
pr|nt('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
iﬂa'(iﬂ$/12)/7
Ins) print('BankofGrin9ottsghresBusinesUabiIItyInsuranceof:
print(‘YourRequestedlnsuranoeOalmA|nounthastobepa6d
vwiY")
print('Amounttnpaytheforlnsu'anoeCIaimAmountpes'
yeah ﬁlm)
loa-input('Doyouwantmamtinuethe lnsuranoeﬁaim
application? (Y/n): ')
if loa=='y':
cursor.execute('update accounts set
Insurance-"uue",insuraooe__type-='buQness',buﬂdir\g_name-%s,cause_of_daim-%
s,med_death_cert_no=%s,ins1rar\oe_amount-%s,lnsuance_no_be_paid_per_year-
%s where id-=%s and usemame-%s',(em,ca,de,ins,ina,I,name))
o0n.oommlt()
wiﬂwlIIIIIBIIBIIIIBISIISIIIII8II8IIIIIBI')
print("Insurance Claim Taken‘)
wnw-----------=------------u--------=-'>
else:
print("Insurance Oalm Aborted‘)
mm1'------------------------------------')
else:
MﬂwicanIII3:13:InlnnhsnaniaiianllluznI')
print("lnsurance Already Oaimed 1!")
wmwlﬂﬂiI88IIBIII8II8IIIIIIBIIISIII8II8I')
ellf d'|I=6:



q='select "‘ from amounts where id=%s and usemame=%s'
wlwr-e><e<11re(q.(i.name))
a=wrsor.fetchall()
for x in a:
print(‘Account Number: ",x{0])
D"l"t('"'"'""""'"-"-"""-"-")
print("Account Holder's Name: ': ",x[1])
l*rifIl('----—'--——--i--')
print("Aooount Holder's Usemame': ",x[2])
mi‘------------—~'>
prlnt("Acnount Balance: “,x[4])
r>I'iI\l('-—-—--—--—-————')
print("Aooount Holder Age: ",x{5])
r>rivw('~—-—-———-—-----—')
print(‘Aooount Holder's Gender: ",x[6])
|:m('--—----------'>
print("Aocount Holder's Number: ',x(7])
wm1'--—--—-—---~'>
print('A0uount Holder's street address: ",x[8])
:>rw<‘——-~»-------~—--'>
print("Aocount Holder's dstrict address: ",x[91)
PﬂﬂI('-—----—-----------')
print('Aooount Holdefs pin code address: ',x[10])
prm'——~—---------~')
print("Aocount Holder's state: ',x[11])
WM‘-----—---—---—-----')
print('Aa:ount Holdefs country: ",x[12])
r>rint('-----------—-'-—-—')
print("KYC: ',x[13])
P'i"l('-""""-'—-""""""""')
print("Aocount Holder's Nominee: ",x[14])



.X[Z°])
.X[Z4])
princc---------—--')
print(“Aocount Holder's Government id For KYC: ",x[15])
print('-- -------- ----------')
print("Account Holder's Government id Number For KYC: ",x[16])
nﬂ'ﬂt( --~----»-------—-'>
r>ﬁnt(‘L0AN= ".X[17])
Pri"¢('—-----—----—-—-----‘)
if x[17]= ='true':
print("Acoount Holder's Loan Type: ',x[18])
wmc---—----—--'>
print(“Aocount Holder's Loan Amount: ",x[19])
Dfi"!(""-""'""'"'"'"'"~"'"')
print("Aocount Holder's Loan Amount to be Paid per Month:
r>ﬁnf('--------------------')
print('Acoount Holder's Loan Duration: ",x[21])
:mrc—--———----- ----- --'>
print("Acoount Holde"s Income Certiﬁcate Number: ",x[22])
mt--—-------~---—'>
print('Aooount Holder's Loan Security: ",x[23])
P*'i"1("'-"**""""‘-"'“'"'""‘-"')
print('A¢munt Holder's Loan Security Number/Weight:
Pfi"t('---------------"-')
print("INSURANCE: ',x[25])
Pfiﬂﬁf‘-—-—----—-—'---—-')
if x[25]= =‘true':
print("Account Holder's Insurance Type: ",x[26])
pmn('----——~—-—-—--v
if x[26]=='ve-hide‘:
print("Acoount Holder's Insurance Amount: ",x[27])
primr ------ -~----————~')



Year: ",x[28])
".X[291)
",x[31])
",x[32])
'.><[331)
Number: ",x[34])
Year: ',x[28])
"-X[351)
print('Aooount Holder's Insurance Amount to be Paid per
prirIt(‘——-——--—--—-—--------—')
print("Aooount Holder's Insurance Vehicle Manufacturer:
print(' --------- ----———-—-----')
print("Account Holder's Irsuranoe Vemde Model: ",x[30])
print('-—-——-----—------—-')
print("Account Holdefs Insurance Vehicle Mode! Year:
pnm('-------------------')
print("Account Holder's Insurance Vehide Fuel Type:
mar‘-—---------—----—-'>
print("Aooount Holder's Insurance Vehide Registered State
print('-- ------ -----—--------')
print("Account Holder's Insurance Vehide Registered
print('--------—----—------~')
elif x[26]=='life':
print('Account Holder's Insurance Amount: ",x[27])
print('-i-—---—-------')
print(“Aooount Holder's Insurance Amount to be Paid per
nrint('-—-------------—--—-—'--')
print("Acoount Holder's Medical Certiﬁcate Number:
print('—----——-—--—-—----—----')
print(”Account Holder's em Certiﬁcate Number: ",x[36])
print('—----—-------—---------')
elif x[26]=='property’:
print("Aooount Holder's Insurance Amount: ",x[27])
pm-——-----~--—--'>



Ywr ",X[281)
".X[37])
print(‘AooountHoldel"sInsuranceAmounttobePaidper
PriM('-—---------------')
print("Account Holder's Insurance Property Number:
wm=~——-~~—~—w
print('Acoount Holder's FIR Number (!ncaseofTheRor
°@"\a9¢ W WORRY)! ".X[33])
mm=-——---~w
elif x[26]=='buslness':
Year: ",x[28])
",X[4°])
print("Account Holders Insurance Amount: ",x[27])
mm=—-—-—-——w
print('AooountHolder'sInsuranoeAn\ounttobePaidper
mm=---—--w
print("Aocount Holder's Insured Building Name: ',x[39])
|>rinl(‘-—----—--—---—--—-')
print("Aceount Holdeﬂs Insurance Amount Claiming Cause
mm=————————~——v
print("Aocount Holder's Insurance Amount Oaimlng
Medical/Death Certiﬁcate Number: ",x[41])
elif chc =7:
P'5"!('--'"-""-"-"--"-')
q='select balance from accounts where id=-%s and usemame-%s'
oursor.execute(q,(i,name))
a=cursor.fecd\a!l()
a=-a[0]
forxina:
print("8alanoe :- ",x)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
elif ch‘-8:
c=0



else:
l>rint("Wr0ﬂ9 096°" ")
print(‘>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
i"'¢e'f=¢¢()
elif d1oloe= =2:
prirm('FILL THESE DETAILS TO CREATE YOUR ACCOUNT)
idea=random.randint(1,100)
name=input("Enner your name : ")
username=input(‘Enter your usemame : ')
pas=lnput('Enter your password : ')
balanoe=ﬂoat(input('Enter your balance : '))
age=lnt(input(‘Enter your age : '))
gender=input('Enter your gender (M/F) : ')
mob=int(input(‘Enter Mobile no. : '))
sh'eet=input('Enter your street name: ')
district=input(‘Enter your District: ')
pincode=int(lnput('Enter your Pincode: '))
state=lnput('Enter State: ')
country=input(‘Enter your Country: ')
nominee=input("Enl:er Nominee Name (lncase alter Death the Account
Credentials has to be handed Over): ")
prin:<'=====-==--===========================')
kyc='false'
loan=‘false‘
insurance=‘false'
query='insert lnto aooouns
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,%s,null,nu
ll,null,nul|,null,null,nu|l,%s,null,null,nulI,null,null,null,null,nu|l,null,null,null,null,nulI,nul
l,null,nuIl);'
value=(ldea,name,usemame,pas,balanoe,age,9ender,mob,street,dlstrict,pinoode,stat
e,country,kyc,nominee,loan,insuranoe)
cursor.a<ecute(query,value)
con.oomrnlt()



wnm'=======-======-=======-=======-=-===')
print(‘Bank Account Successfully Created’)
elif cholce==3:
us=input("Enter your usemame :- ")
P=(i"P\K("EﬂlEf Your P3$$W°"¢ I-'))
pﬂntc”:sass:ax:as2ass:nzzsazauzlsaasaazaaam)
value=(us,p)
query='select ' from accounts where usemame=%s and password=%s "
cursor.e.xecute(query,value)
data_login~cursor.fetchall()
oursor.execute('delet2 from accounts where id=%s and
usemame%s',(data_login[0][0],data_login[0][21))
oon.oommit()
mn:<'====-==-======-=====-===-======-==-==-=='>
print(‘Bank Account Successfully O0sed')
elifchoicem-4:
print('TOLL FREE NO - 18001234567890‘)
pm"--========-==-==--=-=---=---=----===--'>
eiifchoice==S:
bank-=0
else:
Pfi"f('W"0"9 0l>!i0"')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>‘)