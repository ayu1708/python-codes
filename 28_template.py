letter = '''Hello <NAME>
You are selected 
DATE : <DATE>'''
name = input("Enter your name : ")
date = input("Enter date : ")
letter = letter.replace("<NAME>",name)
letter = letter.replace("<DATE>",date)
print(letter)