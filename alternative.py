str_base=input()

for i in range(0,len(str_base)):
    if i%2==0:
        print(str_base[i].upper(),end="")
    else:
        print(str_base[i].lower(),end="")

print("")

strList=str_base.split()

for i in range(0,len(strList)):
    if i%2==0:
        print(strList[i].lower(),end="")
    else:
        print(strList[i].upper(),end="")
    print(" ",end="")
print("")
