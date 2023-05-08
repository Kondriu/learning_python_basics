import os
import csv

curent_dir = os.getcwd()        #get current dir
output_dir_path = os.path.join(curent_dir, 'output')
os.makedirs(output_dir_path, exist_ok=True)     #make dir
csv_file_path = os.path.join(output_dir_path, 'drivers.csv')

with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Jimm', 21, True, False])