from abc import ABC, abstractmethod

from numpy import character
from pip import main

# Strategy Interface
class WeaponStrategy(ABC):
    @abstractmethod
    def use_weapon(self):
        pass

# Strategy concrete classes
class FistStrategy(WeaponStrategy):
    def use_weapon(self):
        return 'hit with fist!'


class KnifeStrategy(WeaponStrategy):
    def use_weapon(self):
        return 'hit with knife!'


class HammerStrategy(WeaponStrategy):
    def use_weapon(self):
        return 'hit with hammer!'


# Context class
class Character:
    def __init__(self) -> None:
        self.weapon = FistStrategy()
    

    def set_weapon(self ,weapon):
        self.weapon = weapon

    
    def fight(self):
        print(self.weapon.use_weapon())


character = Character()
character.fight()
character.set_weapon(KnifeStrategy())
character.fight()
character.set_weapon(HammerStrategy())
character.fight()