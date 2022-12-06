"""
Package representation module
"""
from itertools import zip_longest
from random import randint


class Package:
    """
    Logical representation of data package
    """
    def __init__(self, size, no):
        self.name: str = f'#{no}'
        self.no = no
        self.size: int = size
        self.curr_size: int = size

    def get_size_as_string(self, my_format: str = 'kB') -> str:
        """
        Get formatted package size.
        :param my_format: str
        :return: str
        """
        if my_format == 'B':
            return f'{self.size}B'
        if my_format == 'kB':
            return f'{round(float(self.size)/1024, 2)}kB'
        if my_format == 'MB':
            return f'{round(float(self.size)/1048576, 2)}MB'
        return 'bad format'

    def get_name(self, my_format: str = 'kB'):
        return f'{self.name}, s:{self.get_size_as_string(my_format)}'

    def get_progress_as_string(self):
        return f'{round(100 - ((float(self.curr_size) / self.size) * 100) ,1)}%'

    def upload(self, b_uploaded: int) -> bool:
        self.curr_size -= b_uploaded
        if self.curr_size < 0:
            return True
        else:
            return False


class PackageManager:
    """
    Class responsible for generating packages
    """
    @staticmethod
    def generate_packages(number_of_packages: int,
                          sizes: list = None,
                          sizes_ranges: tuple = (1024, 1048576)) -> list[Package]:
        """
        Get generated list of packages
        :param number_of_packages: int
        :param sizes: list
        :param sizes_ranges: tuple(int,int)
        :return: list[Package]
        """
        if sizes is None:
            sizes = []
        package_list = []
        for pkg_num, size in zip_longest(range(number_of_packages), sizes):
            if size:
                package_list.append(Package(size, pkg_num))
            else:
                package_list.append(Package(randint(sizes_ranges[0], sizes_ranges[1]),
                                            pkg_num))
        return package_list
