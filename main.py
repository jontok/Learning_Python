from code import *
from yahoo_users import *


def __main__():
    user_input = str(input("Enter a Number and Press return: "))
    while user_input != "exit":
        match user_input:
            case "1":
                print_Even_Number()
                break
            case "2":
                print(numbers_x)
                last_same_as_first(numbers_x)
                print(numbers_y)
                last_same_as_first(numbers_y)
                break
            case "3":
                print(my_str)
                print(str(spider_counter(my_str, sub_str)) + "x " + sub_str)
                break
            case "4":
                print(list1)
                print(list2)
                print(combine_lists(list1, list2))
                break
            case "5":
                print(random_greeting())
                break
            case "6":
                print(answers_to_markdown())
                break
            case "7":
                print(who_uses_yahoo("yahoo.com"))
                break
            case _:
                print("Ops")

    __main__()

    

__main__()