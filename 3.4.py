import csv


ii = {
    'А сам как?': 'норм',
    'Алеша': 'Попович',
    'Да все как обычно, жена, дочка, кредит, ипотека, зарплату задерживают второй месяц на заводе, сын клей нюхать начал, но не сознается, хорошо хоть в стране все хорошо': 'а, ну ладно'
}

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for key in ii.keys():
        writer.writerow({'question' : key, 'answer' : ii.get(key)})
