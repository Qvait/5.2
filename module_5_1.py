class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            print(f"Мы на этаже {new_floor}")
        else:
            print("Нет такого этажа")
    def __len__(self):
            return Home.number_of_floors

    def __str__(self):
            return str(f"Название:{self.name}, Этажей:{self.number_of_floors}")



Home = House("Скибиди", 21)

print(Home.number_of_floors, Home.name)
Home.go_to(20)
Home.go_to(23)

print(len(Home))
print(Home)