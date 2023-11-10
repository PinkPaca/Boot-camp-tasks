swimming_time=int(input("please enter the time taken to complete swimming:"))
cycling_time=int(input("please enter the time taken to complete cycling:"))
running_time=int(input("please enter the time taken to complete running:"))

total_time=swimming_time+cycling_time+running_time

if total_time<=100:
    print("Provincial Colours.")
elif total_time<=105:
    print("Provincial Half Colours")
elif total_time<=110:
    print("Provincial Scroll")
else:
    print("No award")