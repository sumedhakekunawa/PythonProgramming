class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        print(self.name, self._age)

    def __set_age__(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be in between 20 and 80')

    def __get_age__(self):
        return self._age


if __name__ == '__main__':
    p = Person('Sumedha', 33)
    p.display()
