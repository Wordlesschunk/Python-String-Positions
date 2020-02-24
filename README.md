# Python-String-Positions
This code asks the user for a string, and then displays the odd and even positions of the string they entere. 
For example if a user was to enter the word: "Hamburger" the program would display the positions of this word
Odd Positions: H m u g r
Even Positions: abre

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
