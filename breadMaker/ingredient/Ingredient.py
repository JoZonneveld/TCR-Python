class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def ingredient_list():
    return [
        # Ingredient('Broodje', 0.40),
        Ingredient('Kaas', 0.20),
        Ingredient('Ham', 0.22),
        Ingredient('Tomaat', 0.10),
        Ingredient('Ei', 0.17),
        Ingredient('Sla', 0.14),
        Ingredient('Kipfilet', 0.25),
        Ingredient('Salami', 0.21),
        Ingredient('Komkommer', 0.11),
        Ingredient('Augurk', 0.10),
    ]


def find_ingredient(name):
    for ingredient in ingredient_list():
        if ingredient.name.lower() == name.lower():
            return ingredient
