from tkinter import *
from models.Customer import CustomerManager
from models.Thread import ThreadManager
from View.ThreadViewer import ThreadViewer


class ViewManager:
    def __init__(self):
        self.root = Tk()
        self.root.title("Simulation")
        self.window_width = 1000
        self.simulation = []

        #Canvas
        self.canvas = Canvas(self.root, width=self.window_width, height=1000, bg="#000000")
        self.canvas.grid(column=0, row=0, rowspan=3)

        #Customer Manager
        self.customer_manager = CustomerManager(6, self)
        self.add_customer = Button(self.root, text="Add Customer", command=CustomerManager.add_customer, padx=50, pady=50)
        self.add_customer.grid(column=1, row=0, sticky='ew')

        #Thread Manager
        self.thread_manager = ThreadManager(4, self)
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

        self.thread_viewer.draw_threads()
        self.canvas.update()
        self.root.after(1000, self.update)
