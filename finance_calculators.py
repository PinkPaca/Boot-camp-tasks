import math

print("inverstment\t- to calculate the amount of interest you'll earn on your inverstment")
print("bond\t\t- to calculate the anount you'll have to pay on ahome loan")
calculation=input("\n Enter either 'investment' or 'bond' from the menu above to proceed:")

if calculation.lower()=="investment":
    P=int(input("please enter the amount of money that you are depositing:"))
    #P is the amount that the user deposits.
    r=int(input("please enter the interest rate:"))
    #r is the interest. it should be invided by 100.
    t=int(input("please enter the number of years you plan on investing:"))
    #t is the number of years that the money is being invested.
    interest=input("Enter 'simple' or 'compound'")
    if interest.lower()=="simple":
        A=P*((r/100)*t+1)
        print(A)
    elif interest.lower()=="compound":
        A=P*math.pow((1+(r/100)),t)
        print(A)
elif calculation.lower()=="bond":
    P=int(input("please enter the present value of the house. e.g. 100000:"))
    #P is the present value of the house.
    intr=int(input("please enter the interest rate. e.g.7:"))
    #intr is the annual interest rate. it should be divided by 12 later.
    n=int(input("please enter the number of months you plan to take to reapy the bond. e.g.120:"))
    #n is the number of months over which the bond will be repaid.

    i=(intr/100)/12

    repayment=(i*P)/(1-math.pow((1+i),(-n)))
    print(repayment)

