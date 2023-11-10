user_fullname=input("Please enter your full name:")

if len(user_fullname)==0:
    print("You haven't entered anything. Please enter your full name.")
elif len(user_fullname)<4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(user_fullname)>25:
    print("You have entered more than 5 charaters. Please make sure that you have only entered your full name.")
else:
    print("Thank your for entering your name.")
    