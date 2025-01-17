import csv
from asyncore import write
import re
import sys

def add(i):
    with open('data.csv','a+',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

def remove(i):
    def save(j):
        try:
            # Open the file in write mode ('w' for overwrite)
            with open('data.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in j:
                    writer.writerow(item)
        except Exception as e:
            print(f"Error saving file: {e}")

    new_list = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)

    save(new_list)                            

def update(i):
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for item in j:
                writer.writerow(item)

    new_list = []
    telephone = i[0]

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    telephone = i[2]
                    email = i[3]
                    address = i[4]

                    data = [name,telephone,email,address]
                    Index = new_list.index(row)
                    new_list[Index] = data

    update_newlist(new_list)

def search(i):
    data = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    return data
