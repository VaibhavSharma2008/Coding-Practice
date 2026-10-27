course1=int(input("Enter course1 marks: "))
course2=int(input("Enter course2 marks: "))
course3=int(input("Enter course3 marks: "))
total=course1+course2+course3
average=total/3
percentage=total/3
grade=str()
if course1>=80 and course3>=65 and course3>=50:
    print("pass")
else:
    print("fail")
    