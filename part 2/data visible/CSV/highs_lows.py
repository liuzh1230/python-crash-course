import csv

filename = "C:/Users/36132/Desktop/python learning/Python crash course/part 2/data visible/CSV/sitka_weather_07-2021_simple.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)