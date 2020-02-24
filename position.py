# This program asks the user for a string and then finds the odd and even positions
# Created By Dylan Jennings 24/02/2020

def separate_string(sentence):
    l = list(sentence)
    list_even = list()
    list_odd = list()
    index = 0

    for letter in l:
        if index % 2 != 0:
            list_even.append(letter)
        else:
            list_odd.append(letter)
        index += 1

    string_even = "".join(list_even)
    string_odd = " ".join(list_odd)

    print("Odd Positions:",string_odd)
    print("Even Positions:",string_even)


print("Hello, Please enter a string!")
separate_str = input()
print("[DEBUG]",separate_str)

separate_string(separate_str)


