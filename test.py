import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# читаем CSV файл и смотрим как
# работают атрибуты и метод.
csvfile = open('names.csv', newline='')
reader = csv.DictReader(csvfile)
print('Диалект: ', reader.dialect)
print('Следующая строка: ', reader.__next__())
print('Прочитано строк: ', reader.line_num)
print('Имена полей: ', reader.fieldnames)
csvfile.close()
