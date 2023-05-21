import sys
import os


def main():
    cook_book = {}

    read_from_file('recipes.txt', cook_book)

    try:
        user_dishes, persons_count = get_task_from_user()
    except:
        sys.exit()

    shop_list = get_shop_list_by_dishes(user_dishes, persons_count)



def read_from_file(path, destination):

    with open(path, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredients_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                }
                ingredients.append(ingredient)

            file.readline()
            destination[dish_name] = ingredients
    # print(destination)


def get_task_from_user():
    dishe_names = []
    while True:
        new_dish = input('Введите название блюда (Оставьте пустым для завершения): ')
        if new_dish:
            dishe_names.append(new_dish)
        else:
            break
    try:
        persons = int(input('На скольких человек? '))
    except ValueError:
        print('Количество персон нужно ввести целым числом.')

    return dishe_names, persons


def get_shop_list_by_dishes(dishes, person_count):



if __name__ == "__main__":
    main()