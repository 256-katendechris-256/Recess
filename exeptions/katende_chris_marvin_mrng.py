from tkinter import *
from datetime import datetime

receipt_number = 1  # Initial receipt number
products = []  # List to store products and their details

def add_product():
    product_name = product_entry.get()
    price = float(price_entry.get())
    quantity = int(qty_entry.get())
    subtotal = price * quantity

    product = {'name': product_name, 'price': price, 'quantity': quantity, 'subtotal': subtotal}
    products.append(product)

    # Clear the input fields
    product_entry.delete(0, END)
    price_entry.delete(0, END)
    qty_entry.delete(0, END)

def print_receipt():
    global receipt_number

    shop_name = "Kriz shop"
    shop_location = "13th Street, Kyoto"
    shop_contacts = "Phone: +256 7735 66789, Email: mugiwaraz@yahoo.com"

    top = Toplevel()
    top.geometry("400x400")
    top.config(background='white')

    # Get current date and time
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    l = Label(top, text='--------------Receipt------------------')
    l.grid(row=0, columnspan=4)
    l.config(background='white')

    shop_info = Label(top, text=shop_name)
    shop_info.grid(row=1, columnspan=4)
    shop_info.config(background='white')

    location_info = Label(top, text=shop_location)
    location_info.grid(row=2, columnspan=4)
    location_info.config(background='white')

    contacts_info = Label(top, text=shop_contacts)
    contacts_info.grid(row=3, columnspan=4)
    contacts_info.config(background='white')

    receipt_info = Label(top, text='Receipt No:')
    receipt_info.grid(row=4, column=0)
    receipt_info.config(background='white')

    receipt_number_label = Label(top, text=f'{receipt_number}', fg='red')
    receipt_number_label.grid(row=4, column=1)
    receipt_number_label.config(background='white')

    date_info = Label(top, text=f'Date: {current_date}', anchor='w')
    date_info.grid(row=5, column=0, columnspan=2)
    date_info.config(background='white')

    time_info = Label(top, text=f'Time: {current_time}', anchor='e')
    time_info.grid(row=5, column=2, columnspan=2)
    time_info.config(background='white')

    heading = Label(top, text='PRODUCT', width=15)
    heading.grid(row=6, column=0)
    heading.config(background='white')

    price_heading = Label(top, text='PRICE', width=10)
    price_heading.grid(row=6, column=1)
    price_heading.config(background='white')

    qty_heading = Label(top, text='QTY', width=5)
    qty_heading.grid(row=6, column=2)
    qty_heading.config(background='white')

    total_heading = Label(top, text='TOTAL', width=10)
    total_heading.grid(row=6, column=3)
    total_heading.config(background='white')

    # Display the products
    row = 7
    for product in products:
        name = product['name']
        price = product['price']
        quantity = product['quantity']
        subtotal = product['subtotal']

        item = Label(top, text=name)
        item.grid(row=row, column=0)
        item.config(background='white')

        item_price = Label(top, text=price)
        item_price.grid(row=row, column=1)
        item_price.config(background='white')

        item_qty = Label(top, text=quantity)
        item_qty.grid(row=row, column=2)
        item_qty.config(background='white')

        item_total = Label(top, text=subtotal)
        item_total.grid(row=row, column=3)
        item_total.config(background='white')

        row += 1

    # Update receipt number for the next receipt
    receipt_number += 1

    # Calculate and display the total
    total = calculate_total()
    total_label = Label(top, text=f'Total: {total}', font=('Arial', 14, 'bold'))
    total_label.grid(row=row, column=2, columnspan=2)
    total_label.config(background='white')

    # Add "Thank you" message
    thank_you_label = Label(top, text='Goods once sold are not returnable\nThank you', font=('Arial', 12, 'italic'))
    thank_you_label.grid(row=row+1, column=0, columnspan=4)
    thank_you_label.config(background='white')

def calculate_total():
    total = sum(product['subtotal'] for product in products)
    return total

root = Tk()
root.geometry("400x200")

product_label = Label(root, text='Product:')
product_label.grid(row=0, column=0)
product_entry = Entry(root)
product_entry.grid(row=0, column=1)

price_label = Label(root, text='Price:')
price_label.grid(row=0, column=2)
price_entry = Entry(root)
price_entry.grid(row=0, column=3)

qty_label = Label(root, text='Quantity:')
qty_label.grid(row=0, column=4)
qty_entry = Entry(root)
qty_entry.grid(row=0, column=5)

add_button = Button(root, text='Add Product', command=add_product)
add_button.grid(row=1, columnspan=2)

print_button = Button(root, text='Print Receipt', command=print_receipt)
print_button.grid(row=1, column=2, columnspan=2)

root.mainloop()
