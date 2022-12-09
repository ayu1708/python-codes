from ctypes import sizeof


myDict= {
    "Ayush": "aGood Boy",
    "Bajaj": "A reputative college",
    "cricket":{'bats':'ball'},
    "marks" : [1,2,3,4],
    2:"A number",
    3:[2,3,2],
    4.3:[2,232,342]
}
print(myDict.keys())
print(type(myDict))
print(type(myDict.keys()))
print(myDict.values())
print(type(myDict.values()))
print(myDict.items())
print(type(myDict.items()))
#print(sizeof(myDict.keys()))
print(myDict)
update_dict={
    "lavish": "friend",
    "Redmi": "Mobile",
    1:2
}
myDict.update(update_dict)
print(myDict)