class Person(object):
    #__slots__ = ('_name', '_age', '_gender')
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    @name.setter
    def name(self,name):
        self._name = name

    def play(self):
        if self._age <=16:
            print("%s正在玩飞行棋."%self._name)
        else:
            print("%s正在玩斗地主." %self._name)

def main():
    person = Person('王大锤',12)
    person.play()
    person.age = 18
    person.name = "王多余"
    person.play()
    print(person.name)
    person._is_gay = True  # AttributeError: 'Person' object has no attribute '_is_gay'
    print(person._is_gay )
if __name__ == '__main__':
    main()




