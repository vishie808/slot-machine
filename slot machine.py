import random

def spin_row():
    symbols = ['🚓', '🚗', '🚕', '🚙', '🛺', '🛻']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0] == "🚓":
            return bet * 10
        elif row[0] in ['🚗', '🚕', '🚙', '🛺', '🛻']:
            return bet * 3
        
    return 0

def main():
    print("Welcome to Slot Machine!! 🤑🤑🤑🤑🤑🤑🤑🤑🤑")

    balance = 100
    print(f"Your starting balance is {balance}$")

    while balance > 0:

        bet = int(input("Enter your bet amount: "))
        

        if bet > balance:
                print("You have insufficient funds!")

        elif bet < 0:
                print("Enter only positive amount!")
                
        else:

            row = spin_row()
            print("Spinning...\n")
            print_row(row)
            balance -= bet

            payout = get_payout(row, bet)
            balance += payout
           

            if payout > 0:
                 print(f"You won {payout}$")
            else:
                 print("You lost this round!")
            
            if balance > 0:
                 print(f"You have {balance}$ left")
            elif balance == 0:
                print("You have lost all your money!!!")
                respawn = input("Wanna press the magic button to refill your money?! (Y/N): ").upper()
                if respawn == 'Y':
                    balance = 100
                    print(f"Your balance has been refilled! Your new balance is {balance}$")
                else:
                    print("Thanks for playing! Goodbye!")
                    break
                               

if __name__ == "__main__":
    main()