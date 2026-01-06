import sys
import random
import time


numbers = ["2", '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace"]

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

def draw_card():
    num = random.choice(numbers)
    suit = random.choice(suits)
    return (num, suit)


def card_value(card):
    num, suit = card
    if num in ["Jack", "Queen", "King"]:
        return 10
    elif num == "Ace":
        return 11
    else:
        return int(num)
    

def hand_value(hand):
    total = 0
    ace = 0
    for num, suit in hand: 
        if num in ["Jack", "Queen", "King"]:
            total += 10
        elif num == "Ace":
            total += 11
            ace += 1
        else:
            total += int(num)

    while ace > 0 and total > 21: 
        total -= 10
        ace -= 1
    return total
    

time.sleep(0.5)
print("Welome to BlackJack")

money = 100 

while True:
    if money <= 0:
        print("You're out of money! Game Over.")
        sys.exit()
    choice = input("Testing your luck? (y/n)")
    if choice.lower() != "y":
        sys.exit()
    elif choice.lower() == "y":
        
        time.sleep(1)
        print("You have", money, "$ to play.")
        bet = int(input("How much do you want to bet? (1-{}): ".format(money)))
        if 1 <= bet <= money: 
            money -= bet
            print("You bet", bet, "$!", "Current money:", money, "$")
        else:
            print("Invalid bet amount.")
            continue
            
        print("Dealing Cards", end=".", flush=True)
        time.sleep(1)

        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), draw_card()]

        print("\nYour cards:", player_hand, "Value:", hand_value(player_hand))
        time.sleep(1)
        print("Dealer's 1st card:", dealer_hand[0])
        time.sleep(1)

        while hand_value(player_hand) < 21: 
            move = input("Hit or Stand? (h / s): ")
            if move.lower() =="h":
                time.sleep(1)
                new_card = draw_card()
                player_hand.append(new_card)
                print("You drew:", new_card, "Value:", hand_value(player_hand))
                time.sleep(1)
            else:
                break
        if hand_value(player_hand) > 21:
            print("Bust!!! You Lose.")
            continue

        print("Dealer's hand:", dealer_hand, "Value:", hand_value(dealer_hand))
        while hand_value(dealer_hand) < 19:
            another = draw_card()
            dealer_hand.append(another)
            time.sleep(1)
            print("Dealer drew:", another, "Value:", hand_value(dealer_hand))
            time.sleep(1)

        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)

        if dealer_total > 21 or player_total > dealer_total:
            money += bet*2
            print("You Win!", "Total Money:", money, "$")
            time.sleep(1)
        elif player_total < dealer_total:
            print("You Lose!", "Total Money:", money, "$")
            time.sleep(1)
        else:
            money += bet
            print("It's a Tie!", "Total Money:", money, "$")
            time.sleep(1)   
        


        
        


