from dataclasses import dataclass, field
from random import choice
from string import ascii_letters


@dataclass(order=True)
class Student:
    sort_index: any = field(init=False, repr=False)
    first_name: str
    second_name: str
    email: str = field(init=False)
    guid: str = field(default_factory=lambda: Student.generate_guid(), init=False, repr=False)
    tuition: int = field(default=0, repr=False)

    @staticmethod
    def generate_guid():
        string = ascii_letters
        result = ''
        for _ in range(15):
            result += choice(string)
        return result

    def __post_init__(self):
        self.email = f'{self.first_name.lower()}.{self.second_name.lower()}@uni.edu'
        self.sort_index = (-self.tuition, self.second_name, self.first_name)
