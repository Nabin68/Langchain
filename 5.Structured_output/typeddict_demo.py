from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int
    
new_person : Person = {"name":"Nabin","age":12 }

print(new_person)