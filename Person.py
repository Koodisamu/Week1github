class Person:
<<<<<<< HEAD
    name = None
    age = None

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

   
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


=======
    def __init__(self, city, address, phone_number):
        self._city = city
        self._address = address
        self._phone_number = phone_number

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f'Address: {self._address}\nCity: {self._city}\nPhone: {self._phone_number}'
>>>>>>> person
