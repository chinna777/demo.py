import csv
print('hi')
lt_csv_data=[]
with open('data4.csv', 'r') as f:
    print("Reading the data from CSV file")
    reader = csv.reader(f)
    lt_csv_data = list(reader)