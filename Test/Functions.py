# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

#print(type(documents))



# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
# # d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;


def people(x):

    for number_doc in documents:
        if number_doc["number"] == x:
            return (number_doc["name"])
    else:
        print('Ошибка')

#print(people("10006"))
# print(people("2207 876234"))

def shelf(y):
    #y = input('Введите номер документа ')
    for elements in directories.items():
        for number_doc in elements[1]:
            if number_doc == y:
                return (elements[0])
    else:
        print(f'Для документа {y} нет места на нашей полке')

#print(shelf("2207 87623"))

def list_doc():
    list_list = []
    for elements in documents:
        list_list.append(elements)
    return list_list
        #print(f'{element["type"]} {element["number"]} {element["name"]}')
#print(list_doc())

def add_doc(type_doc, number_doc, name_boss, number_shelf):
    #type_doc = input('Введите тип документа ')
    #number_doc = input('Введите номер документа ')
    #name_boss = input('Введите имя владельца ')
    #number_shelf = input('Введите номер полки ')
    if number_shelf in directories:
        doc_doc = {"type": type_doc, "number": number_doc, "name": name_boss}
        documents.append(doc_doc)
        directories[number_shelf].append(doc_doc["number"])
        return documents, directories
    else:
        print("Упс. Нету полки дарагой")


#add_doc('Multipass', '2921', 'Конон Варвар', '3')
#print(documents)
#print(directories)

def delete_doc(m):
    #m = input('Введите номер документа ')

    for i, d in enumerate(documents):
        if d["number"] == m:
            documents.pop(i)

            for key, value in directories.items():
                if m in value:
                    value.remove(m)
                    return print(documents, directories)
    print('Нет такого номера')


#delete_doc("2207 876234")

def move_doc_shelf(number_doc, number_shelf):
    #number_doc = input('Введите номер документа  ')
    #number_shelf = input('Введите номер целевой полки  ')
    for key, value in directories.items():
        if number_doc in value:
            value.remove(number_doc)
            directories[number_shelf].append(number_doc)
            return print(f'Документ был перемещен на целевую полку {number_shelf}\n')
        else:
            print("Вы ввели несуществующий номер полки")
#move_doc_shelf("11-2", "3")
#print(documents)
#print(directories)












