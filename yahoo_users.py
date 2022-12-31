import csv

def counting_users(table: str,line_count: int,provider: str,c: int):
    for row in table:
        line_count = line_count+1    
        if provider in row[4]:
            c = c+1
    return [line_count, c]        

def who_uses_yahoo(provider: str):
    with open('table.csv') as csv_file:
        table = csv.reader(csv_file, delimiter=',')
        line_count = 0
        c = 0
        counters = counting_users(table,line_count,provider,c)
        line_count = counters[0]
        c = counters[1]

        percentage = round(100 * c/line_count, 2)
        return percentage

# print(who_uses_yahoo("yahoo.com")) 