print('Задача № 1')

with open('OF0.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        ingred_count = int(file.readline().strip())
        ingred = []
        for _ in range(ingred_count):
            ing = file.readline().strip().split(' | ')
            ingred_name, quantify, measur = ing
            ingred.append({'ingredient_name': ingred_name, 'quantify': quantify, 'measur': measur})
        file.readline()
        cook_book[dishes] = ingred

    print(cook_book)

print()

print('Задача № 2')

def get_shop_list_by_dishes(dishes, person_count):
    new_dishes_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingr_name = ingredient['ingredient_name']
            if ingr_name not in new_dishes_dict.keys():
                new_dishes_dict[ingr_name] = {"measur": ingredient['measur'],
                                              "quantify": int(ingredient['quantify']) * person_count}
            else:
                new_dishes_dict[ingr_name]['quantify'] += person_count * int(ingredient['quantify'])

    return new_dishes_dict

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4))

print( )

print('Задача № 3')

with open('1.txt', 'rt', encoding='utf-8') as f1:
    r = f1.readlines()
    r1 = len(r)
    l_list1 = ['1.txt', r1, r]

with open('2.txt', 'rt', encoding='utf-8') as f2:
    t = f2.readlines()
    t2 = len(t)
    l_list2 = ['2.txt', t2, t]

with open('3.txt', 'rt', encoding='utf-8') as f3:
    d = f3.readlines()
    d3 = len(d)
    l_list3 = ['3.txt', d3, d]

list_list = [l_list1, l_list2, l_list3]

def sort_list_list(len_str):
    return len_str[1]

list_list.sort(key=sort_list_list)

print(f' Итоговый файл: \n {list_list}')

with open('result.txt', 'w', encoding='utf-8') as file:
    print(*list_list, file=file, sep="\n" )


















