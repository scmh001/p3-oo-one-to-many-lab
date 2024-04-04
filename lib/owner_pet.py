

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    
    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet.")
        pet.owner = self  # Assign the Owner instance to the Pet's owner attribute
        self._pets.append(pet)
        
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
    

class Pet:
    
    PET_TYPES = [
        "dog", 
        "cat", 
        "rodent", 
        "bird", 
        "reptile", 
        "exotic"
        ]
    
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner:
            owner.add_pet(self) # automatically add this pet to owners list
