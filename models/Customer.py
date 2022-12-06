import random
import time

from models.package import PackageManager, Package


class Customer:
    def __init__(self, no, number_of_packages: int = 0, sizes: list = None):
        self.name = f'#{no}'
        self.no = no
        self.number_of_packages = number_of_packages
        if self.number_of_packages == 0:
            self.number_of_packages = random.randint(1, 10)
        self.packages: list[Package] = PackageManager.generate_packages(self.number_of_packages, sizes)
        self.is_taking_part_in_auction = False
        self.time_created = time.time()

    def __eq__(self, other):
        return self.name == other.name

    def get_package(self) -> Package:
        return self.packages.pop(0)

    def get_time_in_que(self):
        return self.time_created-time.time()

    def get_packages_as_string(self):
        packages = ''
        for p in self.packages:
            packages += f'{p.get_name()}\n'
        return packages

    def calc_weight(self):
        return self.packages[0].size * (len(self.packages)/self.number_of_packages) * (1 / self.get_time_in_que())


class CustomerManager:
    def __init__(self, number_of_customers, view_manager):
        self.customers = []
        self.no_customers = 0
        self.view_manager = view_manager
        for _ in range(number_of_customers):
            self.add_customer()

    def add_customer(self):
        if len(self.customers) >= 20:
            print("Maximum number of customers")
            return
        self.customers.append(Customer(self.no_customers))
        self.no_customers += 1
        return

    def get_customers_not_in_auction(self):
        c = [x for x in self.customers if not x.is_taking_part_in_auction]
        for x in c:
            x.is_taking_part_in_auction = not x.is_taking_part_in_auction
        return c

    def remove_customers_with_no_packages(self):
        self.customers[:] = [x for x in self.customers if not len(x.packages) == 0]

