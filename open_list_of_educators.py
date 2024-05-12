import csv
def get_names():
    a = """№ - ФИО\n"""
    num = 0
    with open("./data/list.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            name = " ".join(row).split(';')[1]
            # print(row)
            if num != 0:
                a = a + str(num) + " - " + name + "\n"
            num+= 1
    return a


