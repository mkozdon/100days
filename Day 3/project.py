print(
    """
'                           (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\\
                            (_)                 /  \  /\\
                    ________[_]________      /\/    \/  \\
           /\      /\        ______    \    /   /\/\  /\/\\
          /  \    //_\       \    /\    \  /\/\/    \/    \\
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \\
 /\/\/\/       //_______\       \|__|      \\
/      \      /XXXXXXXXXX\                  \\
        \    /_I_II  I__I_\__________________\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~"""
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
left_right = input("Type 'left' or 'right'\n")
if left_right == "right":
    print("Game Over")
    exit()

print("You've come to a lake. There is an island in the middle of the lake.")
swim_wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
if swim_wait == "swim":
    print("Game Over")
    exit()

print("There are three doors.")
door = input("Select one of the doors: red, blue, yellow")

if door == "yellow":
    print("you've WON!")
else:
    print("Game Over")
    exit()
