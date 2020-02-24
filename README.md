# Python-String-Positions (Odd & Even)
# About
A simple script that takes a string and then displays the odd and even positions. 

```
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
    
separate_string("Hamburger")
```
# Input
To change the input of the function edit the separate_string(``"Hamburger"``)
