#Parent class creation

from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod                                               #abstraction on the eat method
    def eat(self):
        pass

    extinct = False

#subclass creation

class Owl(Bird):                                                   #inheritance

    def reproduce(self):
        self.babies += 6                                           #overriding

    def eat(self):
        return "Peck peck"

#creation of another subclass

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1