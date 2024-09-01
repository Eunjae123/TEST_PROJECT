inventory = []
def game_clear():
    return
def game_over():
    pass    
import random
def redo():
    print("game over, play again?")
    choice = input("type yes for yes or no for no")
    if choice.lower() == 'yes':
        print("restarting game")
        init_game()
    elif choice.lower() == 'no':
        print("thanks for playing")
    else:
        print("pick form the choices")
def fight_dragon():
    print("you approach the dragon and attack")
    damage = random.randint(1,100)
    print("you dealt", damage, "damage to the dragon")
    if damage >= 99:
        print("you win!")
        game_clear()
    else:
        print("you lose game over")
        game_over()
def river_path():
    print("you find a sword, press pick to pick up or leave to leave it")
    choice = input("pick or leave")
    if choice.lower() == 'pick':
        if 'sword' not in inventory:
            inventory.append('sword')
        elif choice.lower() == 'leave':
            print("you walk away")
        else:
            print("pick form the 2 options")
            river_path()
        print("there is nothing more to do you go to the cave")
        cave_path()


def cave_path():
    print("you find a dragon sleeping in the cave")
    print("type fight to fight or run to run")
    choice = input("choose")
    if choice.lower() == 'fight':
        if 'sword' in inventory:
            fight_dragon()
        else:
            print("find a sword first. type river to go to the river to find the sword or run away to run away")
            cave_path()
    elif choice.lower() == 'river':
        print("you return to the river")
        river_path()
    elif choice.lower() == 'run away':
        print("you try to run but die GAME OVER")
        game_over()
    else:
        print("pick from the choices")
        cave_path()
def init_game():
    print("Welcome")
    print("You're in a forest, with 2 paths")
    print("type cave to explore cave or river to folllow the river")

    choice = input("what do you choose")
    
    if choice.lower() == 'cave':
        cave_path()

    elif choice.lower() == 'river':
        river_path()
    else:
        print("choose from the 2 options")
        init_game() #recursion
init_game()
