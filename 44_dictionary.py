myDict= {
    "Ayush": "aGood Boy",
    "Bajaj": "A reputative college",
    "cricket":{'bats':'ball'},
    "marks" : [1,2,3,4],
    2:"A number",
    3:[2,3,2],
    4.3:[2,232,342]
}
print(myDict['Ayush'])
print(myDict["Bajaj"])
print(myDict["cricket"]["bats"])
print(myDict["marks"])
print(myDict[2])
print(myDict[3])
print(myDict[4.3])
myDict["Ayush"]="Enterprenuer"
print(myDict)