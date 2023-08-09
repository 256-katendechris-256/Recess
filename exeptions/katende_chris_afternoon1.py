#exception handling
"""Exceptions: Exceptions are raised when the program is syntactically correct,
 but the code results in an error. This error does not stop the execution of the program,
 however, it changes the normal flow of the program.
 
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module
 """

#catching typeError
a=6
b="age"
try:
    c=a+b
except TypeError:
    print("TypeError occurred and cann't add integer to string") 
finally:
    print("the finally block will execute regardless if there was any exceptions")

#catching indexError
my_list=[10,"hello",34]
#negative indexing starts from -1 as last element has position =-1
index=-2 

try:
    value= my_list[index]
    print(value)
    #this line raises IndexError because list doesn't have that

    anotherValue= my_list[-5]
    print(anotherValue)
    #line so this except block won't be executed

    thirdValue= my_list[7]
    print(thirdValue)
    #also out of range hence raising Index Error
except IndexError:
    print('IndexError Occurred')
    
#catching KeyError
dict={
    "name":'John',
    'age':28,
    'height':43
    
}
key='gender'   ##not present in dict keys
try:
    val=dict[key]
    ###accessing non existing key
    print (val)
    ####This code wont run since it's inside the try block which catches only specific errors
except:
    print("key does not exist")



# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")

#using try with else
def div(c,d):
      try:
            k=((c+d)/(c-7))
      except:
            print("can not divide with zero its a math syntax error")      
      else:
            print ("value is",k )

     
div(7,13)
div(8,13) 

#raising exceptions
#try:
     
     # raise NameError ("Name error occured here")
#except NameError:
      #print ('An exception occurred')
   #   raise Exception()   ##this will reaise any type of expection raised in above line

#file handling 
file = open('text.txt','r')

for each in file:
      print(each)

#reading from a file
# Python code to illustrate read() mode
file = open("text.txt", "r")
print (file.read())

# Python code to create a file
file = open('text.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#or
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
	f.write("Hello World!!!")

# Python code to illustrate append() mode
file = open('text.txt', 'a')
file.write("This will add this line")
file.close()


