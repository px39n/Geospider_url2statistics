import csv
import platform
import sys



def write_csv(path, data):
    with open(path,"a+",encoding='utf-8',newline='') as csvfile: 
        writer = csv.writer(csvfile)
    #先写入columns_name
        writer.writerow(data)
    