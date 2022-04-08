from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Pig(Animal):
    def eat(self):
        print("I eat plants and other animals")


class Tiger(Animal):
    def eat(self):
        print("I eat only other animals")


class Zebra(Animal):
    def eat(self):
        print("I eat only plants")


class Giraffe(Animal):
    def eat(self):
        print("I eat only plants")


class Fox(Animal):
    def eat(self):
        print("I eat plants and other animals")


class Shark(Animal):
    def eat(self):
        print("I eat only other animals")
