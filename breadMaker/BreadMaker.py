from breadMaker.ingredient.Ingredient import find_ingredient, ingredient_list, Ingredient


def get_name_list(l):
    return list(map(lambda x: x.name, l))


def get_price_list(l):
    return list(map(lambda x: x.price, l))


class BreadMaker:
    def __init__(self):
        self.ingredients = []

    def __add_ingredient(self, name):
        new_ingredient = find_ingredient(name)
        if new_ingredient is not None:
            self.ingredients.append(find_ingredient(name))
            print(name, 'added')
        else:
            print(name, 'not found')

    def calculate_price(self):
        prices = get_price_list(self.ingredients)
        return round(sum(prices), 2)

    def create(self):
        done = False
        self.ingredients.append(Ingredient('Broodje', 0.40))
        while not done:
            print('Wat wil je op je broodje: ', get_name_list(ingredient_list()))
            print('Dit heb je nu:', get_name_list(self.ingredients))
            new_ingredient = input()
            self.__add_ingredient(new_ingredient)
            print('Verder nog iets? (y/n)')
            done = True if input() == 'n' else False
            print('')  # Enter

        print('Dat word dan', self.calculate_price(), 'Euro')


def run():
    bread = BreadMaker()
    bread.create()
