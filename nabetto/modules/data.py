import csv

def gather(obj):
    with open('data.csv', mode='a') as f:
        data_writer = csv.writer(f)
        data_writer.writerow([*obj])