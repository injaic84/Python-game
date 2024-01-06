from room import Room
from character import Enemy
from game import play_game

# Rooms description
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room, buzzing with flies")

ballroom = Room("Ballroom", has_enemy = True )
ballroom.set_description("A fancy ballroom")

dining_hall = Room("Dining Hall",has_enemy =True)
dining_hall.set_description("A fancy dining hall")

# This links the kitchen to the dining hall
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Naming the Characters
dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)
alex = Enemy("Alex", "The wizard")
ballroom.set_character(alex)

dave.set_conversation("Hi my name is Dave, Id like to eat your brain.")
dave.set_weakness("cheese")
alex.set_conversation("If you win this game, I will not turn you into a burger.")


current_room = kitchen
while True:
   print("\n")
   current_room.get_details()
   inhabitant = current_room.get_character()
   if inhabitant is not None:
        inhabitant.describe()
        if inhabitant == alex:
            play_game()
        elif inhabitant == dave:
            print("What will fight with?")
            fight_with = input("\n> ")
            dave.fight(fight_with)
         
        print("Which direction would you like to go? North, east, south, west")
   command = input("\n> ")
   if command in ["north", "east", "south", "west"]:
    current_room = current_room.move(command)
   elif command == "fight":
    if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                dead = True 
