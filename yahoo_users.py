import csv



def who_uses_yahoo(provider):
    with open('table.csv') as csv_file:
        table = csv.reader(csv_file, delimiter=',')
        line_count = 0
        c = 0
        for row in table:
            line_count = line_count+1    
            if provider in row[4]:
                    c = c+1                

        
        percentage = round(100 * c/line_count, 2)
        return percentage

print(who_uses_yahoo("yahoo.com"))