#Working with csv files
import csv

with open("contacts.csv") as contacts:
    csv_reader = csv.reader(contacts, delimiter = ",")
    for row in csv_reader:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}')

print("\n\n")

print("Second loop")

#reading csv into a dictionary
with open ("contacts.csv") as contacts:
    csv_reader = csv.DictReader(contacts)
    for row in csv_reader:
        print(row)
        # print(row.keys())
        # print(f'{row["name"]} {row["address"]} {row["email"]} {row["phone"]}')

print("End second loop")

'''
optional parameters
delimiter - character used to separate each field
quotechar - character used to surround fields
'''

with open ("contacts2.csv") as contacts:
    csv_reader = csv.reader(contacts, delimiter = "|", quotechar = "'", escapechar = "\\")
    for row in csv_reader:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}')


#writing csv files
with open ("orders.csv", "w") as order_file:
    order_writer = csv.writer(order_file, delimiter = ",")

    #Header columns
    order_writer.writerow(['OrderNo', 'ItemId', 'Description', 'Qty'])
    #Data
    order_writer.writerow(['100', '34', 'AAA batteries', 6])
    order_writer.writerow(['200', '57', 'Dish soaps', 8])
    order_writer.writerow(['200', '86', 'Apples', 12])

#writing csv files from a Dictionary
with open ("movies.csv", "w") as movie_file:
    fields = ['title', 'rating', 'runtime']
    writer = csv.DictWriter(movie_file, fieldnames=fields)

    writer.writeheader() #Write the header column names
    writer.writerow({'title' : 'Interstellar', 'rating' : 'PG-13', 'runtime' : 169 })
    writer.writerow({'title': 'Batman', 'rating': 'All', 'runtime': 135})
    writer.writerow({'title': 'Dunkirk', 'rating': 'MA', 'runtime': 153})


