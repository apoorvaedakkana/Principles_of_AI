# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Derived class for Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Bow!"

# Derived class for Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
