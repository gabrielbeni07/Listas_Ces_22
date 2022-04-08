import math


class Hamburguer:
    def _init_(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def _repr_(self):
        return(f'Hamburguer({self.radius!r},' f'{self.ingredients!r})')

    def area(self):
        return self.bread_area(self.radius)

    @classmethod
    def traditional(cls):
        return cls(['meat', 'chesse', 'salad'])

    @classmethod
    def bacon(cls):
        return cls(['meat', 'chesse', 'salad', 'bacon'])

    @staticmethod
    def bread_area(r):
        # The bread is a semi sphere
        return 2 * r ** 2 * math.pi
