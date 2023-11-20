# Задача 1
with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_qty = int(file.readline())
        dish_ingredient = []
        for ingredient_line in range(ingredients_qty):
            ingredient_dict = {}
            item1, item2, item3 = file.readline().split(" | ")
            ingredient_dict['ingredient_name'] = item1.strip(' ')
            ingredient_dict['quantity'] = item2.strip(' ')
            ingredient_dict['measure'] = item3.strip(' ')
            dish_ingredient.append(ingredient_dict)
        file.readline()
        cook_book[dish_name] = dish_ingredient
    # print(cook_book)

# Задача 2
def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']] += int(ingredient['quantity']) * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measuare': ingredient['measure'],
                                                             'quantity': (int(ingredient['quantity']) * person_count)}

    print(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача 3
# def rewriting(file_for_writing: str):
#     filenames = ["1.txt", "2.txt", "3.txt"]
#     files = {}
#
#     for name in filenames:
#         with open(name, 'r', encoding='utf-8') as f:
#             lines = f.read().splitlines()
#             files[name] = lines
#     # print(files)
#
#     filenames = sorted(filenames, key=lambda n: len(files[n]))
#     # print(filenames)
#
#     with open('result.txt', 'w', encoding='utf-8') as f:
#         for name in filenames:
#             lines = files[name]
#             count = len(lines)
#             f.write(f'{name}\n{count}\n')
#             for i, line in enumerate(lines):
#                 f.write(f'Строка номер {i + 1} файла {name}: {line}\n')
#
#
# file_for_writing = 'result.txt'
# rewriting(file_for_writing)