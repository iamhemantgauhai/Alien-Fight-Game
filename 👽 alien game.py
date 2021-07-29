from random import randint
stamina = 10
def report(stamina):
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")

# main function - accepts your input for fight with the alien
def fight(stamina): # stamina
    while stamina > 0:
      # won't enter this loop ever. The function will always return False.
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run >>> ")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "1" in response or "2" in response:
            less = randint(0, stamina)
            stamina -= less # subtract random int from stamina
            report(stamina) # see function above
        elif "3" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "4" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
    return False

print ("A threatening alien wants to fight you!\n")
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive==0:
	print("Congrats!! Finally you killed the alien.")
else:
	print("Sorry!! Alien killed you.")