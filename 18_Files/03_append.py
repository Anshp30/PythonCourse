#Append to an existing  file name john Doe.txt
#It should conatin data about john doe Home Town.

f = open("john Doe.txt","a")
string = '''
He lived in newyork!!
'''
f.write(string)
f.close()