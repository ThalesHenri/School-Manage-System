from person import Person
import random


class Student(Person):
    def __init__(self, name, cpf, address, international):
        super().__init__(name, cpf, address)
        # self.registration = registration
        self.international = False
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        id_len = 8
        b = " "
        for i in range(id_len):
            a = random.choice(chars)
            b += a
        self.registration = b
