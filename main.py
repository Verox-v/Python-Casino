import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("**************")
    print(" |  ".join(row))
    print("**************")

def spin_roulette():
    colors = ["🟩", "⬛", "🟥"]
    return [random.choice(colors) for _ in range(1)]

def print_roulette(spin):
    print("**************")
    print(" | ".join(spin))
    print("**************")

def roulette_payout(spin, bet, color_choice):
    if spin[0] == color_choice:
        if spin[0] == "🟩":
            return bet * 10
        elif spin[0] == "⬛":
            return bet * 3
        if spin[0] == "🟥":
            return bet * 5
    return 0

def slot_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 50
    return 0 

           

def main():
    balance = 50
    while True:
        print("***********************************")
        print("=====Welcome to Python Casino!=====")
        game_choice = input("You've got 2 games to choose:\n1.Python Slots\n2.Python Roulette\n3.Exit\nEnter your choice: ")
        print("***********************************")

        if game_choice == "1": 
            print("******************************")
            print("Welcome to Python Slot Machine")
            print("Symbols:🍒 🍉 🍋 🔔 ⭐")
            print("******************************")

            while balance > 0:
                print(f"Your balance is ${balance}")

                bet = input("How much do you want to bet?: ")

                if not bet.isdigit():
                    print("Please input a valid number")
                    continue
                bet = int(bet)

                if bet > balance:
                    print("You cannot bet more than you've got")
                    continue
                if bet <= 0:
                    print("You cannot bet less than 0")
                    continue

                balance -= bet

                row = spin_row()
                print("Spinning...")
                print_row(row)

                payout = slot_payout(row, bet)
                
                if payout > 0:
                    print(f"Your payout is ${payout}")
                else: 
                    print("Sorry, you lost this round")

                balance += payout

                play_again = input("Do you want to bet again? (Y/N) ").upper()
                
                if play_again == "Y" or "N":
                    if play_again == "N":  
                        break
            print(f"Exiting to menu. Your balance is ${balance}!")

        elif game_choice == "2":
            print("**************************")
            print("Welcome to Python Roulette")
            print("Colors: 🟩 ⬛ 🟥 ")
            print("**************************")
                    
            while balance > 0:
                print(f"Your balance is ${balance}")

                bet = input("How much do you want to bet?: ")

                if not bet.isdigit():
                    print("Please input a valid number")
                    continue
                bet = int(bet)

                if bet > balance:
                    print("You cannot bet more than you've got")
                    continue
                if bet <= 0:
                    print("You cannot bet less than 0")
                    continue

                

                color_choice = input("Which color do you want to bet?: ").upper()
                if color_choice == "GREEN":
                    color_choice = "🟩"
                elif color_choice == "RED":
                    color_choice = "🟥"
                elif color_choice == "BLACK":
                    color_choice = "⬛"
                else:
                    print("Enter a valid color")
                    continue
                balance -= bet
                
                spin = spin_roulette()
                print("Spinning...")
                print_roulette(spin)

                payout = roulette_payout(spin, bet, color_choice)
        
                if payout > 0:
                    print(f"Your payout is ${payout}")
                else: 
                    print("Sorry, you lost this round")

                balance += payout

                play_again = input("Do you want to bet again? (Y/N) ").upper()
                
                if play_again == "Y" or "N":
                    if play_again == "N":  
                        break
        elif game_choice == "3":
            print("Exiting the program. Have a nice day!")
            break
        else:
            print("Incorrect choice")
            continue
        print(f"Exiting to menu. Your balance is ${balance}!")
if __name__ == "__main__":
    main()