import os
import csv

current_dir = os.getcwd()
out_dir_path = os.path.join(current_dir, 'output')
os.makedirs(out_dir_path, exist_ok=True)
file_path = os.path.join(out_dir_path, 'store.csv')

with open(file_path, 'w', newline='') as csv_file:
    header = ['Product', 'Id', 'Quantity']
    writer = csv.DictWriter(csv_file, header) # headers recured if use dictionary writer
    writer.writeheader() #write hgeaders to the file
    writer.writerow({"Product": "Beans", 'Id': 1, 'Quantity': 3000})
    writer.writerow({"Product": "Bananas",  'Quantity': 100, 'Id': 12})
    writer.writerows([
        {"Product": "Apples",  'Quantity': 300, 'Id': 2},
        {"Product": "Oranges",  'Quantity': 130, 'Id': 3},
        {"Product": "Mango",  'Quantity': 40, 'Id': 4}
    ])