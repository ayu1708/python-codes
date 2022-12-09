a =int(input("Input number : "))
b =int(input("Input number : "))
c =int(input("Input number : "))
if(a>35 and b>35 and c>35):
    if((a+b+c)>120):
        print("Pass")
    else:
        print("fail")
else:
    print("fail")