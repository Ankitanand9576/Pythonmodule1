""" Given a list of grades (values between 0 and 100), use a for loop and if-else statements to convert each numerical grade
to a letter grade (A, B, C, D, F) """
check=True
try:
 while(True):
    markOfStudent=(input("Enter the marks: "))

    if (markOfStudent>90 and markOfStudent<=100):
        print ("grade of student a")
    elif (markOfStudent>70 and markOfStudent<=90):
        print("grade of student is b")
    elif (markOfStudent>50 and markOfStudent<=70):
        print("grade of student is c")
    elif (markOfStudent<=50 and markOfStudent>30):
        print("grade of student is d")
    elif(markOfStudent<=30 and markOfStudent>=0):
        print("grade of student is E")
except Exception as e: 
    print(" Error is :",e)

    

            