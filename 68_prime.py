num = int(input("Enter a Number you want to be check prime or not : "))
prime = True
for i in range (2,num):
    if(num%i==0):
        prime = False
        break
if prime:
    print("Number is prime ")
else:
    print("Number is not prime")
