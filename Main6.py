

# def greet(name:str, age:int) -> None:
#     """"
#     Tato funkce pozdravi uzivatele"""
#     print(f"Hello {name}, you are {age} years old")
#
# greet(age=25, name="Jenda")


# def sum(x:float,y:float) -> float:
#     result = x + y
#     return result
# a = 1
# b = 2.5
# c = sum(a,b)
#
# print(c)

user = {
    "name": "Jenda",
    "age": 25,
    "work_position": "Mechanic",
    "hair_color": "Black"
}

def change_work_position(user: dict, new_work_position: str, hair):
    user['work_position'] = new_work_position
    user['hair_color'] = hair

print(user)
change_work_position(user, "programmer", "Brown")
print(user)
