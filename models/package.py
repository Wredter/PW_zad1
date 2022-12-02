"""
Package representation module
"""
from itertools import zip_longest
from random import randint


class Package:
    """
    Logical representation of data package
    """
    def __init__(self, size, name):
        self.name: str = name
        self.size: int = size

    def get_size_as_string(self, my_format: str = 'kB') -> str:
        """
        Get formatted package size.
        :param my_format: str
        :return: str
        """
        if my_format == 'B':
            return f'{self.size}B'
        if my_format == 'kB':
            return f'{float(self.size)/1024}kB'
        if my_format == 'MB':
            return f'{float(self.size)/1048576}MB'
        return 'bad format'


class PackageGenerator:
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
                package_list.append(Package(f'Package #{pkg_num}', size))
            else:
                package_list.append(Package(f'Package #{pkg_num}',
                                            randint(sizes_ranges[0], sizes_ranges[1])))
        return package_list
