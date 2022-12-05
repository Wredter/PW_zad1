from tkinter import Canvas
from models.Customer import Customer


class CustomerViewer:
    def __init__(self, view_manager):
        self.view_manager = view_manager
        self.global_offset = 550
        self.customer_width = 100
        self.customer_height = 250

    def draw_customers(self):
        canvas: Canvas = self.view_manager.canvas
        customers = self.view_manager.customer_manager.customers
        offset_y = 0
        offset_x = 0
        canvas.create_text(canvas.winfo_width()/2, self.global_offset, text="CUSTOMERS", fill='#FFFFFF', font='Helvetica 16 bold')
        for customer, x in zip(customers, range(len(customers))):
            if x % 10 == 0 and x != 0:
                offset_y += self.customer_height
                offset_x = 0
            self.__draw_customer(canvas, offset_x * self.customer_width, 25 + offset_y + self.global_offset, customer)
            offset_x += 1

    def __draw_customer(self, canvas: Canvas, x: int, y: int, customer: Customer):
        uc = self.view_manager.thread_manager.get_uploading_customers()
        if customer in uc:
            canvas.create_rectangle(x, y, x + self.customer_width, y + self.customer_height, outline='#00FF10')
        else:
            canvas.create_rectangle(x, y, x + self.customer_width, y + self.customer_height, outline='#FFFF00')
        canvas.create_text(x + (self.customer_width / 2), y, text=customer.name, fill='#FFFFFF', font='Helvetica 12 bold')
        canvas.create_text(x + 10, y + 10, text=f'Packages:\n'
                                           f'{customer.get_packages_as_string()}',
                           fill='#FFFFFF', font='Helvetica 8 bold', anchor='nw')
