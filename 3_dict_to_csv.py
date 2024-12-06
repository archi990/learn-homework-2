"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():

    staff = [
        {"name": "Анна", "age": 25, "job": "Программист"},
        {"name": "Иван", "age": 30, "job": "Аналитик"},
        {"name": "Ольга", "age": 28, "job": "Дизайнер"},
        {"name": "Петр", "age": 35, "job": "Менеджер"},
    ]
    with open('staff.csv', 'w', encoding='utf-8') as f:
        fields = ['name','age','job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for people in staff:
            writer.writerow(people)

if __name__ == "__main__":
    main()
