from tkinter import *
from models.Customer import CustomerManager
from models.Thread import ThreadManager
from View.ThreadViewer import ThreadViewer
from View.CustomerViewer import CustomerViewer


class ViewManager:
    def __init__(self):
        self.root = Tk()
        self.root.title("Simulation")
        self.canvas_width = 1000
        self.canvas_height = 1100
        self.tick_time = 100
        self.simulation = []

        #Canvas
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="#000000")
        self.canvas.grid(column=0, row=0, rowspan=3)

        #Customer Manager
        self.customer_manager = CustomerManager(0, self)
        self.customer_viewer = CustomerViewer(self)
        self.add_customer = Button(self.root, text="Add Customer", command=self.customer_manager.add_customer, padx=50, pady=50)
        self.add_customer.grid(column=1, row=0, sticky='ew')

        #Thread Manager
        self.thread_manager = ThreadManager(0, self.customer_manager)
        self.thread_viewer = ThreadViewer(self)
        self.add_thread = Button(self.root, text="Add Thread", command=self.thread_manager.add_thread, padx=50, pady=50)
        self.add_thread.grid(column=1, row=1, sticky='ew')

        #Fill
        self.root.rowconfigure(2, weight=2)

    def run(self):
        self.update()
        self.root.mainloop()

    def update(self):
        self.canvas.delete('all')

        self.customer_viewer.draw_customers()
        self.thread_viewer.draw_threads()
        self.canvas.update()
        self.thread_manager.update(self.tick_time)
        self.root.after(self.tick_time, self.update)
