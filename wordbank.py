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

     for line in range(5):   # each die has 5 lines
          for face in dice:   # loop through each die value
               print(dice_art[face][line], end="  ")  # print that die's line
          print()  # move to next output line


     total = sum(dice)
     
     return f"You rolled: {number} dices and got a total of {total}"









try:
     number_of_dice = (int(input("How many dice/s: ")))
     print(dice_game(number_of_dice))

except ValueError:
     print("Enter numbes only: ")


