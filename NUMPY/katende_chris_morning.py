import tkinter as tk
"""
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    result = eval(expression)
    display.delete(0, tk.END)
    display.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display
display = tk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(window, text=str(i), command=lambda num=i: button_click(num))
    button.grid(row=(9-i)//3+1, column=(i-1)%3)

# Create operator buttons
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, command=lambda op=operator: button_click(op))
    button.grid(row=i+1, column=3)

# Create clear and equal buttons
button_clear = tk.Button(window, text="C", command=button_clear)
button_clear.grid(row=4, column=0)
button_equal = tk.Button(window, text="=", command=button_equal)
button_equal.grid(row=4, column=1)

# Start the main loop
window.mainloop()
  """

#python class to calculate area of a circle
import math

class CircleArea:
    def __init__(self, radius):
        self.__radius = radius
    
    @property 
    def get_area(self): 
        return math.pi * math.pow(self.__radius, 2)

radius = float(input('Enter Radius: '))

circle = CircleArea(radius)  # Pass the radius as an argument when creating the instance

print(f"The Area is {circle.get_area}")


#encapsulation with employee information to give a pay increamention (salary with employee information to new_salary) eg from 850000 to 1000000
class Employee:
    raiseAmount = 150000

    def __init__(self, _firstName, _lastName, pay):
        """Initialize employee's attributes."""
        self.firstName = _firstName
        self.lastName = _lastName
        self.pay = pay

    def fullname(self):
        print("First Name:", self.firstName, "Last Name:", self.lastName)

    def applyRaise(self):
        self.pay += self.raiseAmount
        return self

emp_1 = Employee("John", "Doe", 850000)
print(emp_1.applyRaise().pay)


                                    


