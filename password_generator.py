import random
# Letters, numbers and symbols that password can contain
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User selects how many letters, numbers or symbols they need
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_num = nr_letters + nr_symbols + nr_numbers
letter_counter = 0
symbol_counter = 0
number_counter = 0
passList = [""] * total_num # creating an empty list with total number of elements required

general_counter = 0

while True:
    random_pos = random.randint(0, total_num-1) # selects random position in list

    if passList[random_pos] == "": # if that random position is empty
        if letter_counter < nr_letters: # if the letter counter is less than the number of letters that the user wants then fill it with a random letter
            random_letter = letters[random.randint(0, len(letters)-1)]
            passList[random_pos] = random_letter
            letter_counter += 1
            general_counter += 1
        elif number_counter < nr_numbers:
            random_number = numbers[random.randint(0, len(numbers)-1)]
            passList[random_pos] = random_number
            number_counter += 1
            general_counter += 1
        elif symbol_counter < nr_symbols:
            random_symbol = symbols[random.randint(0, len(symbols)-1)]
            passList[random_pos] = random_symbol
            symbol_counter += 1
            general_counter += 1
    elif general_counter == total_num: # if all the positions in the list is filled then break out of this while loop
        break


password_string = "".join(passList)
print(password_string)
