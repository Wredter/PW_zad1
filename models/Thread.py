from models.Customer import Customer
from models.package import Package


class Thread:
    def __init__(self, transfer_speed: int = 1024):
        self.transfer_speed: int = transfer_speed
        self.current_file_transferred: Package = None
        self.auctioned_customers = []

    def auction(self, customer_list: list[Customer]) -> (Customer, Package):
        c, p = None, None
        return c, p

    def get_available_customers(self, customer_list: list[Customer]):
        for customer in customer_list:
            if not customer.is_taking_part_in_auction:
                customer.is_taking_part_in_auction = not customer.is_taking_part_in_auction
                self.auctioned_customers.append(customer)

    def return_customers(self):
        for customer in self.auctioned_customers:
            customer.is_taking_part_in_auction = not customer.is_taking_part_in_auction
        self.auctioned_customers = []
