from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hi my name is Dave, Id like to eat your brain.")
dave.talk()
dave.set_weakness("cheese")
print("What will fight with?")
fight_with = input("\n> ")
dave.fight(fight_with)


alex = Enemy("Alex", "The Wizard")
alex.describe()
alex.set_conversation("If you win this game, I will not turn you into a burger.")
alex.talk()
alex.set_play_game()
print("Are you ready to play?")
