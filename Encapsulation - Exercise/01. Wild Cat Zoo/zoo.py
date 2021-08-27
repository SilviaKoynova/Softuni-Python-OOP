class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = sum([a.money_for_care for a in self.animals])
        if total <= self.__budget:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        lions = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Lion"]
        result.extend([f"----- {len(lions)} Lions:"])
        result.extend(lions)

        tigers = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Tiger"]
        result.extend([f"----- {len(tigers)} Tigers:"])
        result.extend(tigers)

        cheetahs = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result.extend([f"----- {len(cheetahs)} Cheetahs:"])
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        keepers = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Keeper"]
        result.extend([f"----- {len(keepers)} Keepers:"])
        result.extend(keepers)

        caretakers = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Caretaker"]
        result.extend([f"----- {len(caretakers)} Caretakers:"])
        result.extend(caretakers)

        vets = [a.__repr__() for a in self.workers if a.__class__.__name__ == "Vet"]
        result.extend([f"----- {len(vets)} Vets:"])
        result.extend(vets)

        return "\n".join(result)


# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet
# from project.zoo import Zoo
#
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())

