student_name="praveen"
marks=[85,78,92,88,75]
total=0
for mark in marks:
    total=total+mark
    average=total/len(marks)
    percentage=(total/500)*100
    print("student name:",student_name)
    print("marks:",marks)
    print("total marks:",total)
    print("average:",average)
    print("percentage:",percentage)
    if percentage >=90:
        print("grade:,A+")
    elif percentage >=80:
        print("grade:,A")
    elif percentage >=70:
        print("grade:,B")
    else:
        print("grade:,C")    