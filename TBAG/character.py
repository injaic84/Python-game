class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.combat_item = None
        self.current_room = None  # Initialize the character in no room
        
# Describe the character
    def describe(self):
        print(f"{self.name} is here")
        print(self.description)

# Move Character into rooms
    

# Set what the character will say when talked to 
    def get_conversation(self):
        return self.conversation

    def set_conversation(self, conversation):
        self.conversation = conversation

# Talk to the character 
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}says]:{self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")
        
# Fight the enemy
    def fight(self, combat_item):
        print(f"{self.name} does not want to fight you.")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.current_room = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off, using {combat_item}.")
            return True 
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False
        
    def set_choices(self, choice_1, choice_2,choice_3):
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        

   
    
        