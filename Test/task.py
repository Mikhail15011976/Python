geo_logs = [{
    'visit1': ['Москва', 'Россия']
}, {
    'visit2': ['Дели', 'Индия']
}, {
    'visit3': ['Владимир', 'Россия']
}, {
    'visit4': ['Лиссабон', 'Португалия']
}, {
    'visit5': ['Париж', 'Франция']
}, {
    'visit6': ['Лиссабон', 'Португалия']
}, {
    'visit7': ['Тула', 'Россия']
}, {
    'visit8': ['Тула', 'Россия']
}, {
    'visit9': ['Курск', 'Россия']
}, {
    'visit10': ['Архангельск', 'Россия']
}]

def task_1():
    new_logs = []
    for elements in geo_logs:
        for keys, values in elements.items():
            if values[1] == 'Россия':
                new_logs.append(elements)
    #for visit in new_logs:
    #    print(visit)
    return new_logs
#print(task_1())

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def task_2():
    rezult = set(sum(ids.values(), []))
    rezult_final = list(rezult)
    return rezult_final

#print(task_2())

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def task_3():
    max_val = max(stats.items())
    return max_val[0]
#print(task_3())

