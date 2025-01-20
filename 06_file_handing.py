### File Handling ###
import os
# .txt file

txt_file = open("my_file.txt", "w+") # Leer y Escrbir
txt_file.write("Mi nombre es Fernando\nMiApellido es Flores\nTengo 20 Years\nY mi lenguaje preferido es Python.")
# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta kotlin")
print(txt_file.readline())

txt_file.close()

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("my_file.txt")

# .json file

import json

json_file = open("my_file.json", "w+")

json_test = {
    "name": "Fernando",
    "lastname": "Flores",
    "age": 20,
    "languages": ["Python", "Kotlin", "Swift"],
    "website": "https://fernandoflores.dev"
}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
import csv

csv_file = open("my_file.csv", "w+")

csv_write = csv.writer(csv_file)

csv_write.writerow(["name", "lastname", "age", "languages", "website"])

csv_write.writerow(["Fernando", "Flores", 20, "Python", "https://fernandoflores.dev"])

csv_write.writerow(["Roswell", "", 2, "COBAL",""])

csv_file.close()



with open("my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)