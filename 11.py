ii = {
    'А сам как?': 'норм',
    'Алеша': 'Попович',
    'Да все как обычно, жена, дочка, кредит, ипотека, зарплату задерживают второй месяц на заводе, сын клей нюхать начал, но не сознается, хорошо хоть в стране все хорошо': 'а, ну ладно'
}

def ask_user():
    ii_keys = ii.keys()
    input_text = ''
    output_text_default = 'Как дела?'
    output_text = output_text_default
    while input_text != 'Хорошо':
        try:
            input_text = input(f'{output_text}\n').strip()
            output_text = ii.get(input_text, output_text_default)
        except KeyboardInterrupt:
            print('Ну пока!\n')
            break

ask_user()
