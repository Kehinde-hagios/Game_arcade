import guess_game
import RPS_Game
import duty_call_game
import random

def game_run():
    new_choice = random.choice(["fancy", "great", "nice", "capable"])
    player_name = input("\nHmmm Young Adventurer What's the name?\n").title()
    print(f"\nHmm Hmm {player_name}... What a {new_choice} name")
    print("")
    while True:
        print("SELECT".center(24, "="))
        print("1".ljust(5, ".") + "🎲 Guess".rjust(18, " "))
        print("2".ljust(5, ".") + "🪨  🧻 ✂️  RPS".rjust(18, " "))
        print("3".ljust(5, ".") + "🥷 🩸 Duty Call".rjust(18, " "))
        print("4".ljust(5, ".") + "👋 Quit".rjust(18, " "))

        choice = input("")

        if choice not in ["1", "2", "3", "4"]:
            print(f"SELECT A VALID GAME {player_name}!!")
            continue

        choice_new = int(choice)

        if choice_new == 1:
            guess_game.key(player_name)
        elif choice_new == 2:
            RPS_Game.key(player_name)
        elif choice_new == 3:
            duty_call_game.key(player_name)
        elif choice_new == 4:
            print("Well That's it.... Enjoy")
            break
game_run()
