from random import randint

#● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘" 

dice_art = {
    1: ( "┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘" ),
    2: ( "┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘" ),
    3: ( "┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘" ),
    4: ( "┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘" ),
    5: ( "┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘" ),
    6: ( "┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘" )
}

def dice_game(number: int) -> str:


     dice = [randint(1,6) for num in range(number)]

     for die in range(number):
          for dices in dice_art.get(dice[die]):
               print(dices)

     total = sum(dice)
     
     return f"You rolled: {number} dices and got a total of {total}"









try:
     number_of_dice = (int(input("How many dice/s: ")))
     print(dice_game(number_of_dice))

except ValueError:
     print("Enter numbes only: ")


