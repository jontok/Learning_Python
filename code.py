import json
import random

string = "schokolade"

def print_Even_Number():
	# your code
    c = 0
    for i in string:
        if (c % 2):
            print(i)
        c = c +1 
        
# print_Even_Number()

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def last_same_as_first(numbers):
    # your code
    if numbers[0] == numbers[len(numbers)-1]:
        print("True")

#last_same_as_first(numbers_y)

my_str = "Spiderman is not even a real spider"
sub_str = "spider"
def spider_counter(my_str, sub_str):
    my_str = my_str.lower()
    return my_str.count(sub_str)
 
# print(spider_counter(my_str, sub_str))

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def combine_lists(list1,list2):
    list3 = []
    for i in list1:
        if (i % 2):
            list3.append(i)
    for i in list2:
        if not (i % 2):
            list3.append(i)
    return list3

# print(combine_lists(list1, list2))
def random_greeting():
    file = open("data.json")
    data = json.load(file)
    return data["greetings"][random.randint(0, len(data["greetings"])-1)]

    # return greeting

# print(random_greeting())

def answers_to_markdown():
    file = open("data.json")
    data = json.load(file)
    c = 1
    print("| Number | Answer |")
    print("| ---- | --- |")
    for i in data["responses"]["answers"]["5"]["answer"]:
        print(f"| { c } | { i } |")
        c = c+1

# answers_to_markdown()

