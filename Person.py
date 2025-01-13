class Person:
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


