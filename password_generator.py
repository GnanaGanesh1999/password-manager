import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 7)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = ''
    total_chars = nr_numbers + nr_letters + nr_symbols

    while total_chars > 0:
        selector = random.randint(1, 3)
        if selector == 1 and nr_letters > 0:
            password += random.choice(letters)
            nr_letters -= 1
        elif selector == 2 and nr_symbols > 0:
            password += random.choice(symbols)
            nr_symbols -= 1
        elif selector == 3 and nr_numbers > 0:
            password += random.choice(numbers)
            nr_numbers -= 1
        total_chars = nr_numbers + nr_letters + nr_symbols

    return password
