import csv
import platform
import sys

def write_csv(path, data, way):
    with open("test.csv","w",encoding='utf-8') as csvfile: 
        writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(data)
    