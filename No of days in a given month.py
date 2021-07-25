N=int(input())
if N==0 or N>12:
    print("Error")
elif N==2:
    print("28")
elif N%2==0:
    print("31")
else:
    print('30')