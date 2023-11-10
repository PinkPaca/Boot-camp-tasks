sum=0
number=0
count=0
while number!=-1:
    number=int(input("enter a number: "))
    if number==-1:
        break 
    sum+=number
    count+=1

avg=sum/count
print("Average is "+str(avg))