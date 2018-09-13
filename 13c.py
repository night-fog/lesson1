from random import randint

journal = [
    {
        'class_name': '4a',
        'score_list': [randint(1, 5) for i in range(randint(10, 30))]
     },
    {
        'class_name': '4b',
        'score_list': [randint(1, 5) for i in range(randint(10, 30))]
     },
    {
        'class_name': '4c',
        'score_list': [randint(1, 5) for i in range(randint(10, 30))]
     },
    {
        'class_name': '4d',
        'score_list': [randint(1, 5) for i in range(randint(10, 30))]
     },
    {
        'class_name': '8g',
        'score_list': [randint(1, 5) for i in range(randint(10, 30))]
     }
]

def list_avg(int_list: list):
    return (sum(int_list) / len(int_list))

def avg_school(data: list):
    avg_scores = list()
    for item in data:
        avg_scores.append(list_avg(item.get('score_list')))
    return list_avg(avg_scores)

print(f'School avg={avg_school(journal):0.0f}')
for item in journal:
    print('class {} avg={:0.0f}'.format(item.get("class_name"), list_avg(item.get('score_list'))))
