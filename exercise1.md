# Exersise 1

Print characters from a string that are present at an even index number

## Solution

```python3

def print_Even_Number(string):
    counter = 0
    for index in string:
        if (counter % 2 == 0):
            print(index)
        counter = counter +1 

```
