class Employee:

    def __init__(self, name, password, salary):
        self_name = name
        self_password = password
        self_salary = salary

    @property
    def set_name(self):
        return self._name

    @property
    def password(self):
        raise AttributeError('Password not readable')

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, new_salary):
        self.salary = new_salary


e = Employee("Sumedha", "1234", 2000)
e._name="Sumedha"
e._password = "1234"
e._salary=2000

print(e._salary)
