
import ipdb







class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        self.name = name
        self.owner = owner

        Pet.all.append(self)
            
        


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        if not isinstance(self, Owner):
            raise Exception
        
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def get_sorted_pets(self):
        if not isinstance(self,Owner):
            raise Exception
        
        owned_pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(owned_pets, key=lambda pet: pet.name)
    

