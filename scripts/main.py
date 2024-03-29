from NEATCore import NEATCore
from Game import Game

if __name__ == "__main__":
    print("Starting...")
    core = NEATCore("scripts/config-feedforward.txt")
    game = Game(core , True)  # Pass the NEATCore instance to the Game
    core.set_game(game)  # Set the game instance in NEATCore
    core.run(1000)  
    print("Done!")