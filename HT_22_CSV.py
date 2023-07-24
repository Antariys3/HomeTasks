import json
import csv
import random


def create_phone_number(value: list) -> list:
    # Функция принимает список value и с вероятностью 75% добавляет случайный номер телефона
    # с оператором из списка operators. Возвращает измененный или неизмененный список value.
    random_numb = random.randint(0, 100)
    operators = ['095', '066', '098', '096', '050', '097']
    if random_numb < 75:
        value.append(random.choice(operators) + str(random.randint(0, 9999999)).zfill(7))
    else:
        value
    return value


with open("workers.json") as file:
    dict_workers = json.load(file)

# в Windows нельзя добавлять латиницу и кирилицу в один файл поэтому я заменил 'ID' на 'ИН'
# так же я заменил newline=None на newline="" и delimiter="," на delimiter=";"
# а по хорошему надо Windows заменить на Ubuntu
name_of_fields = ["ИН", "Имя", "Возраст", "Телефон"]
dict_workers = {key: create_phone_number(value) for (key, value) in dict_workers.items()}

with open("workers_csv.csv", "w", newline="") as file:
    f_csv = csv.writer(file, delimiter=";")
    f_csv.writerow(name_of_fields)
    for key, value in dict_workers.items():
        item = [key, *value]
        f_csv.writerow(item)
    # в интернете поискал как это можно сделать оптимизированей и красивее и вот результат:
    # f_csv.writerows([key, *value] for key, value in dict_workers.items())
    # в свой код вставлять не буду, так как это не моё решение, но на будущее запомню.