import csv
from os import name
import matplotlib.pyplot as plt

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

def get_providers():
    with open('table.csv') as csv_file:
        table = csv.reader(csv_file, delimiter=',')
        providers = []
        for l in table:
            provider = l[4].split("@")[1]
            if provider not in providers:
                providers.append(provider)
        return providers

# get_providers()

def plot_providers():
    print("start")
    rest_providers = 0
    percentile_providers = []
    name_providers = []
    for p in get_providers():
        pct = who_uses_yahoo(p)
        if pct > 0.1:
            percentile_providers.append(who_uses_yahoo(p))
            name_providers.append(p)
        else:
            rest_providers = rest_providers + pct
    print(percentile_providers)
    name_providers.append("rest " + str(len(percentile_providers)))
    percentile_providers.append(rest_providers)
    plt.bar(name_providers, percentile_providers)
    plt.xticks(rotation=90)
    plt.show()

plot_providers()
