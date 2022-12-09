senstence =  input("Enter your content : ")
a= senstence.find("make a lot of money")
b= senstence.find("buy now")
c= senstence.find("subscribe this")
d= senstence.find("click this")
if(a==-1 and b==-1 and c==-1 and d==-1):
    print("Not spam")
else:
    print("spam")