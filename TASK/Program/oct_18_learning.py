# # defining a class
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name          # instance attribute
#         self.age = age

#     def greet(self) -> str:
#         return f"Hi, I'm {self.name} and I'm {self.age}."

# # create objects (instances)
# alice = Person("Alice", 30)
# print(alice.greet())            # "Hi, I'm Alice and I'm 30."
# bob = Person("Bob", 25)
# print(bob.greet())              # "Hi, I'm Bob and I'm 25."


# Example: handle missing key with try/except
data = {"a": 1, "b": 2}

# try:
#     value = data["c"]           # may raise KeyError
#     print("Value:", value)
# except KeyError as err:
#     print(f"Key not found: {err}. Using default value 0.")
#     value = 0

value = data["a"]
print("Final value:", value)
