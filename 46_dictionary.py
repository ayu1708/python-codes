dic={
    "Dog":"Kutta",
    "Cat":"Billi",
    "COw":"Gaaye"
}
print("Word in dictionary are",dic.keys())
a=input("Enter the word whose meaning is to be searched : ")
print("Meaning is : ",dic.get(a))