city_info = {
    "city": "Москва",
    "temperature": "20"
}
print(city_info['city'])
city_info['temperature'] = str(int(city_info['temperature']) - 5)
print(str(city_info))

if 'country' in city_info.keys():
    print('Key exists')

city_info.get('country', 'Россия')
city_info['date'] = '27.05.2017'
print(str(len(city_info)))
