# Password Generator Project
import random


class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.nr_letters = random.randint(8, 10)
        self.nr_symbols = random.randint(2, 4)
        self.nr_numbers = random.randint(2, 4)
        self.character_list = [random.choice(self.letters) for _ in range(self.nr_letters)]
        self.symbols_list = [random.choice(self.symbols) for _ in range(self.nr_symbols)]
        self.numbers_list = [random.choice(self.numbers) for _ in range(self.nr_numbers)]
        self.password_list = self.character_list + self.symbols_list + self.numbers_list
        self.password = ""

    def create_password(self):
        random.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        return self.password
