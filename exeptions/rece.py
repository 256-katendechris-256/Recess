import tkinter as tk
from PIL import Image, ImageTk


class ReceiptGenerator:
    def __init__(self):
        self.root = tk.Tk()

        # Creating a label for the image of the receipt and packing it in the root window
        img = Image.open("Receipt_image1.jpg")
        resized_img = img.resize((40, 60))  # Resize the image to 40x60 pixels
        photoimg = ImageTk.PhotoImage(resized_img)
        lblImg = tk.Label(master=self.root, image=photoimg)
        lblImg.grid(row=0, column=0, columnspan=6)

        # Adding text fields for customer details like name, address, phone number, etc.
        txtName = tk.Entry(font=('Arial', 20))
        txtAddress = tk.Text(width=50, height=4, wrap='word')
        txtPhoneNo = tk.Entry()
        txtItemName = tk.Entry()
        txtQuantity = tk.Entry()
        txtPricePerItem = tk.Entry()
        txtSubTotal = tk.Entry()
        txtTaxRate = tk.Entry()
        txtDiscountAmount = tk.Entry()
        txtGrandTotal = tk.Entry()
        btnGenerateReceipt = tk.Button(text="Generate Receipt", command=self.generate_receipt)

        # Grid layout for all the widgets
        txtName.grid(row=1, column=0, columnspan=6, padx=10, pady=(20, 0))
        txtAddress.grid(row=2, column=0, columnspan=6, padx=10, pady=(10, 0))
        txtPhoneNo.grid(row=3, column=0, padx=10, pady=10)
        txtItemName.grid(row=4, column=0, padx=10, pady=10)
        txtQuantity.grid(row=4, column=1, padx=10, pady=10)
        txtPricePerItem.grid(row=4, column=2, padx=10, pady=10)
        txtSubTotal.grid(row=5, column=0, padx=10, pady=10)
        txtTaxRate.grid(row=5, column=1, padx=10, pady=10)
        txtDiscountAmount.grid(row=5, column=2, padx=10, pady=10)
        txtGrandTotal.grid(row=6, column=0, padx=10, pady=10)
        btnGenerateReceipt.grid(row=7, column=0, columnspan=6, pady=(20, 0))

        self.root.mainloop()

    def generate_receipt(self):
        # Retrieve the values from the text fields and perform the necessary actions to generate the receipt
        # You can implement the logic for generating the receipt here
        print("Generating Receipt")


# Create an instance of the ReceiptGenerator class to start the application
receipt_generator = ReceiptGenerator()
