import copy
from models.Customer import Customer
from models.package import Package


class Thread:
    def __init__(self,no: int, transfer_speed: int = 1024):
        self.name = f'#{no}'
        self.no = no
        self.transfer_speed: int = transfer_speed
        self.current_file_transferred: (Package, Customer) = None
        self.auctioned_customers = []
        self.history_of_loads: list[(Package, Customer)] = [] #(Package(1024, 0), Customer(0)), (Package(20000, 1), Customer(0))

    def auction(self, customer_list: list[Customer]) -> (Package, Customer):
        c, p = None, None
        return c, p

    def get_available_customers(self, customer_list: list[Customer]):
        for customer in customer_list:
            if not customer.is_taking_part_in_auction:
                customer.is_taking_part_in_auction = not customer.is_taking_part_in_auction
                self.auctioned_customers.append(customer)

    def get_customers(self):
        for customer in self.auctioned_customers:
            customer.is_taking_part_in_auction = not customer.is_taking_part_in_auction
        self.auctioned_customers = []

    def get_thread_history_as_string(self):
        if not self.history_of_loads:
            return "No files \nhave been loaded"
        history = ""
        for x in self.history_of_loads:
            history += f'{x[1].name},{x[0].get_name()}\n'
        return history

    def get_working_package_as_string(self):
        if self.current_file_transferred is None:
            return f'No file loading \n' \
                   f'Progress: 0%'
        return f'{self.current_file_transferred[1].name},{self.current_file_transferred[0].get_name()}\n' \
               f'Progress: {self.current_file_transferred[0].get_progress_as_string()}'

    def update(self, time):
        uploaded = round(self.transfer_speed * (time / 1000), 0)
        #TODO : add update function



class ThreadManager:
    def __init__(self, number_of_threads, view_manager):
        self.no_threads = 0
        self.threads = []
        self.free_threads = copy.copy(self.threads)
        self.used_threads = []
        self.view_manager = view_manager
        for _ in range(number_of_threads):
            self.add_thread()

    def add_thread(self):
        if len(self.threads) >= 8:
            print("Maximum number of threads")
            return
        self.threads.append(Thread(self.no_threads))
        self.no_threads += 1
        return

    def get_uploading_customers(self):
        customers = []
        for thread in self.threads:
            customers.append(thread.current_file_transferred[1])
        return customers

    def get_free_threads(self):
        free = []
        for thread in self.threads:
            if not thread.current_file_transferred:
                free.append(thread)

    def update(self, time):
        for thread in self.used_threads:
            # TODO: add update function
            pass
