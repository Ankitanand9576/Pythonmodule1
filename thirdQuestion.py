""" Create a program that repeatedly asks the user for a string until the user types "quit". Use a for loop and an 
if-else statement inside it to check if the user input matches "quit" and break the loop if it does """
demoBoolean=True
demoList=[]
while(demoBoolean):
    user=input("Enter any string: ")
    demoList.append(user)
    print(demoList)
    for i in demoList:
      print(f"this is : {i}")
      if (i!="quit"):
        demoBoolean=False
        break
      else:
          break
print(demoList)
#Use for loop
# .append