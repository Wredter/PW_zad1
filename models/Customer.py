from models.package import PackageManager, Package
import time


class Customer:
    def __init__(self, no, number_of_packages: int = 5, sizes: list = None,):
        self.name = f'#{no}'
        self.no = no
        self.packages = PackageManager.generate_packages(number_of_packages, sizes)
        self.is_taking_part_in_auction = False
        self.time_created = time.time()

    def get_package(self) -> Package:
        return self.packages.pop()

    def get_time_in_que(self):
        return self.time_created-time.time()


class CustomerManager:
    def __init__(self, number_of_customers, view_manager):
        self.customers = []
        self.view_manager = view_manager
        for _ in range(number_of_customers):
            self.add_customer()

    @staticmethod
    def add_customer():
        pass
