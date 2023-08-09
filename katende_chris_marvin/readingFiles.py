import sys

"""script,file2 = sys.argv
#openning the file to be opened
txt =open(file2)

#reading all lines in a file
print(f"here is the file you want {file2}")
print(txt.read())

#knowing the python file you are working with
print("\n\tThis is how we know what type of file it is....")
print(script)

#Alternatively
alt =input("insert the file name>> ")
txt1 =open(alt)

print("this is yet another way to read files.....")
print(txt1.read())

#Closing thw file
txt.close()
"""

# Script to read the new file1.txt file that has bee modified
script,file1=sys.argv
txt3 = open (file1,"r+") # opening and reading from the same time
print ("Here's your text: \n", txt3.read(),"\n")
