student = {
    "name": "Nash",
    "age": 20,
    "course": "BSIT"
}

print(student["name"])
student = {"name": "Nash", "age": 20}
student["grade"] = 95
student["age"] = 21
print(student)
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

for key, value in car.items():
    print(key, ":", value)
    phonebook = {
    "Nash": "09123456789",
    "Ericka": "09987654321",
    "Bebu": "09112223333"
}

name = input("Enter name: ").lower()

if name in phonebook:    "Nash": "09123456789",



    print("Number:", phonebook[name])
else:
    print("Name not found")
