#Exercise 1
#slicing in strings
name="Katende"
print(name[0:5])
 #first 4 characters of the string,


#Exercise 2
#for loop in strings
#prints each letter in the string
my_string = "Hello World!"
for letter in my_string :
    print (letter)


#Exercise 3
#determining length of a string
string_length=len("hello")
print(string_length)



#Exercise 4
#code to ask students about their mental health

def get_mental():
    question=int(input(f"On a scale of 1 to 10,\n How are you feeling today?"))
    if (question <=5):
        return "Your mood is low and you feel sad most of the time"
    elif (question >5 and question<=8):
        return "You are very stressed today"
    elif (question >8 and question<=10):
        return "You are not okay and you need help"
    else:
        print("Please enter a number between 0-10")
        # this iterates the code incase a number greater than 10 is inserted 
        return get_mental()
    
response=get_mental()
print(response)


