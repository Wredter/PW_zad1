from models.Customer import Customer
from models.package import Package


class Thread:
    def __init__(self, no: int, transfer_speed: int = 1024):
        self.name = f'#{no}'
        self.no = no
        self.transfer_speed: int = transfer_speed
        self.current_file_transferred: (Package, Customer) = None
        self.auctioned_customers = []
        self.history_of_loads: list[(Package, Customer)] = [] #(Package(1024, 0), Customer(0)), (Package(20000, 1), Customer(0))

    def auction(self, customer_list: list[Customer]) -> bool:
        if customer_list:
            customer_list.sort(key=lambda x: x.calc_weight(), reverse=True)
            self.current_file_transferred = (customer_list[0].get_package(), customer_list[0])
            for customer in customer_list:
                customer.is_taking_part_in_auction = not customer.is_taking_part_in_auction
            return True
        return False

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

    def update(self, time) -> bool:
        uploaded = max(round(self.transfer_speed * (time / 1000), 0), 1)
        if self.current_file_transferred[0].upload(uploaded):
            self.history_of_loads.append(self.current_file_transferred)
            self.current_file_transferred = None
            return True
        return False


class ThreadManager:
    def __init__(self, number_of_threads, customer_manager):
        self.no_threads = 0
        self.threads = []
        #self.free_threads = copy.copy(self.threads)
        self.used_threads = []
        self.free_threads = []
        self.customer_manager = customer_manager
        for _ in range(number_of_threads):
            self.add_thread()

    def add_thread(self):
        if len(self.threads) >= 8:
            print("Maximum number of threads")
            return
        t = Thread(self.no_threads)
        self.threads.append(t)
        self.free_threads.append(t)
        self.no_threads += 1
        return

    def get_uploading_customers(self):
        customers = []
        for thread in self.threads:
            if thread.current_file_transferred is not None:
                customers.append(thread.current_file_transferred[1])
        return customers

    def update(self, time):
        #print("manager_update")
        for thread, x in zip(self.used_threads, range(len(self.used_threads))):
            #print(f"used: thread {thread.name}")
            if thread.update(time):
                self.free_threads.append(self.used_threads.pop(x))
        for thread, x in zip(self.free_threads, range(len(self.free_threads))):
            #print(f"free: thread {thread.name}")
            if thread.auction(self.customer_manager.get_customers_not_in_auction()):
                self.used_threads.append(self.free_threads.pop(x))
                self.customer_manager.remove_customers_with_no_packages()


