# A set of data extracted from a csv file.
# The CSV file (portfolio.csv) contains the following fields pertaining
# to the share price of companies

# Company name,
# number of shares owned,
# Price of each share in the currency it is quoted in (GBP, EUR or USD),
# Total values in £,
# Total cost of these shares when purchased in £,
# Change in value since purchased,
# Change in value since purchase as a percentage of purchase price,
# Price change on the day this record created,
# Currency (always GBP),
# Currency the shre purchased in (GBP, EUR, USD),
# Exchange rate - price of a GBP in the currency in which the shares are published,
# Date that this row was extracted,
# Time that this row was extracted,

# the first line is a title line

# the numeric fields may contain commas.

import csv
from datetime import datetime

to_num = lambda num: float(num.replace(",", ""))
class Portfolio:
    data = {}

    def load(self):
        """ load the file portfolio.csv into the field data """
        with open('portfolio.csv') as csv_file:
            print("Loading portfolio.csv")
            csv_reader = csv.reader(csv_file, delimiter=',')
            first = True
            for row in csv_reader:
                # skip first line
                if first:
                    first=False
                else:
                    self.data[row[0]]={
                        "name": row[0],
                        "shares": int(to_num(row[1])),
                        "price": to_num(row[2])/to_num(row[10]),
                        "value": to_num(row[3]),
                        "cost": to_num(row[4]),
                        "profit": to_num(row[5]),
                        "timestamp": datetime.strptime(row[11]+" "+row[12], "%d-%b-%y %H:%S")
                    }

    def names(self):
        """ return a list of share names """
        return [v['name'] for _,v in self.data.items()]

    def detail(self, key):
        """ return a dictionary of fields pertinent to the specified named share holing"""
        print("detail ", key, "->", self.data[key])
        return self.data[key]

