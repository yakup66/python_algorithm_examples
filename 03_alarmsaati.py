
######## alarm time project

time=int(input("Please write a number"))
if time<7:
    print("keep sleeping")
elif time==7:
    print("alarm is going off. Wake up")
elif time>7:
    print("you're late")
else:
    print("please write a number")

