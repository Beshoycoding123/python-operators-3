maths=int(input("enter your math marks: "))
eng=int(input("enter your english marks: "))
sci=int(input("enter your science marks: "))
history=int(input("enter your history marks: "))
PE=int(input("enter your PE marks: "))
total=maths+eng+sci+history+PE
print("the sum of your marks is",total)
ave=(total/5)
print("the average of your marks is",ave)
if ave>=90 and ave<=100:
    print("your grade is A1")
elif ave>=80 and ave<=90:
    print("your grade is A2")
elif ave>=70 and ave<=80:
    print("your grade is A3")
elif ave>=60 and ave<=70:
    print("your grade is A4")
elif ave>=50 and ave<=60:
    print("your grade is A5")
else:
    print("invalid input")