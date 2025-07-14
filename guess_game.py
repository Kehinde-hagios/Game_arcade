def key(player_name):
    print(f"\nWelcome Young Adventurer to Guess the die 🎲 ")
    print(f"Hmm Hmm {player_name} you really have guts")
    import sys
    import random
    def score():
        count = 0
        player_count = 0
        python_count = 0
        draw_count = 0
        def RPS():
            print("")
            print("SELECT".center(16,"="))
            print("🎲 1".ljust(5,"."))
            print("🎲 2".ljust(5,".") + "or".rjust(14," "))
            print("🎲 3".ljust(5,"."))       
            player_choice = input(f"\n {player_name} Select your choice:\n")
            if player_choice not in ["1","2","3"]:
                print("Select Between 1,2 or 3")
                return RPS()
            
            player = int(player_choice)
            computer_choice = random.choice("123")
            computer = int(computer_choice)

            nonlocal player_count
            nonlocal draw_count
            nonlocal python_count
            print(f"{player_name} choose 🎲 {player} while Python choice 🎲 {computer}")
            if (player == 1 and computer == 3)or (player == 2 and computer == 1)or(player == 3 and computer == 2):
                player_count += 1
                print(f"🥳 {player_name} hmmm lucky guess")
            elif player == computer:
                draw_count += 1
                print("🤝 That's A Tie")
            else:
                python_count += 1
                print("🐍 Python wins\n")
        
            nonlocal count
            count += 1
            print(f"Game Time {count}")
            print("\nDo you want to play Again?")
            while True:
                retry = input("Y  to Continue\nQ  to Quit\n")
                if retry.lower() not in ["y","q"]:
                    print("Input a Valid Option")
                    continue
                if retry == "y":
                    return RPS()
                else:
                    print(f"🎉🎉 Congratulations\n{player_name} won {player_count} out of {count} games")
                    print(f"Python won {python_count} games")
                    print(f"You tied {draw_count} games")
                    print(f"Winning Rate= {player_count/count:.2%}")
                    print("\n\nAlright that's all, returning to arcade...\n")
                    break

        return RPS()
    return score()


