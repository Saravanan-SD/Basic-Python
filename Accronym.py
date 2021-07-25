User_input= str(input("Enter a sentence: "))
text= User_input.split()
a= ""
for i in text:
    a = a+str(i[0]).upper()
print(a)