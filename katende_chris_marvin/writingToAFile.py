import sys
#script ,file1 =sys.argv

#print (f"file u are working with is called {file1}")
#opening the file from the user view

#bat =open(input("File to be opened: "),'w')

#deleting the contents of the file
#bat.truncate()
#writing into a new line in the same file
#bat.write('Hello World!')
#print(bat.read())



luck=input("name of file")
text =open(luck,'w')
text.truncate()

line1=input("Line1: ")
line2=input("Line 2: ")
line3=input("Line 3: ")

#now writing to the file
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)

print("file successfully opened, truncated and written into")

#closing the file
text.close()