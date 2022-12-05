from models.package import PackageGenerator, Package
import time


class Customer:
    def __init__(self, number_of_packages: int = 5, sizes: list = None,):
        self.packages = PackageGenerator.generate_packages(number_of_packages, sizes)
        self.is_taking_part_in_auction = False
        self.time_created = time.time()

    def get_package(self) -> Package:
        return self.packages.pop()

    def get_time_in_que(self):
        return self.time_created-time.time()
