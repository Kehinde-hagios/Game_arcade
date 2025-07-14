def key(player_name):
    print("\nwelcome to duty called zone 🥷🩸\nYour first step to doom\n")

    def play_game():
        score = 0
        x = input("What's the short version of call of duty mobile?\n").lower()
        if x == "codm":
            print("Great🎉")
            score += 1
        else:
            print("loser😒😒 ")

        x = input("Who created the universe?\n").title()
        if x == "God":
            print("✅ indeed you know the truth!")
            score += 2
        else:
            print("for realll?😒😒 ")

        x = input("What's call of duty company called?\n").lower()
        if x == "activision":
            print("Someone really knows his game!👌🥳")
            score += 3
        else:
            print("Fuckkkk!! That simple thing 🤦‍♂️")

        print("Hint: My gamer name 😁😎")
        x = input("What's the developer name?\n")
        if x == "Warlock":
            score += 2
        else:
            print("you sure you are....wop 😒😑 ")

        x = input("What was your name again?\n")
        if x == player_name:
            print("indeed a player")
            score += 2
        else:
            print("bot detected 😒")

        print(f"hahaha {player_name} you really survived")
        print(f"here's your score wop: {score/10:.2%} ")

        while True:
            x = input("u wanna retry? (yes/no) ").lower()
            if x not in ["yes", "no"]:
                print("Input a Valid Option")
                continue
            if x == "yes":
                play_game()
            if x == "no":
                print("Alright that's all, returning to arcade...\n")
                break
    return play_game()