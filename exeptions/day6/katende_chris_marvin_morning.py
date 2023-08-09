#matching and searching
#regex / regular expressions| MAtch first word, Match group word|Match All Numbers

import re
text="hello everyone how are you doing, am 25 years old"
match= re.search(r"^\w*",text)
print(match.group())

#email validator
def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False


em="katende23@gmail.com"
em2="lalaland@gmailcom"

print(validate_email(em))
print(validate_email(em2))


#Generatores and Iterators
def factorial(ne):
    if ne==0:
        return 1
    else:
        return ne * factorial(ne-1)
for xe in range(1,10):
    print(factorial(xe))

def squares():
    for i in range(1,10):
      yield i**2

squares_iterator=squares()

for i in range(5):
    print(next(squares_iterator))

def factorial(num):
    if num==0:
            yield 1
    else:
            yield num * next(factorial(num-1))
for live in range(1,10):
    print(next(factorial(live)))

"""
#decorator
def decorator(func):
        def wrapper():
            print("Before")
            func()
            print("After")
        return wrapper
@my_decorator
def my_function():
"""