import time 

def sling_knife_run_half():
    time.sleep(3)
    response = input("QUICKLY! The monster is coming A) Continue running B) Cut the ropes on the bridge?")
    if response == "A" or response == "a":
        time.sleep(3)
        print("After crossing the bridge, you have no way to stop him chasing you.")
        time.sleep(4)
        print("As he catches up, you accept fate.")
        time.sleep(3.5)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        time.sleep(2)
        print("You cut the rope and the bridge falls in the river, along with the monster.")
        time.sleep(4)
        print("It gets swept away by the current and you are able to escape and get home. YOU WIN!")
    else:
        print("Invalid response")
        sling_knife_run_half()

def knife_bat_run_half():
    time.sleep(3)
    response = input("QUICKLY! The monster is coming A) Continue running B) Cut the ropes on the bridge?")
    if response == "A" or response == "a":
        time.sleep(3)
        print("After crossing the bridge, you have no way to stop him chasing you.")
        time.sleep(4)
        print("As he catches up, you accept fate.")
        time.sleep(2.5)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        time.sleep(2)
        print("You cut the rope and the bridge falls in the river, along with the monster.")
        time.sleep(4)
        print("It gets swept away by the current and you are able to escape and get home. YOU WIN!")
    else:
        print("Invalid response")
        knife_bat_run_half()

def sling_knife_run():
    time.sleep(3)
    print("You come across a draw bridge. The monster is still running after you.")
    time.sleep(3.5)
    response = input("After crossing the bridge do you: A) Continue running B) Cut the ropes on the bridge? ")
    if response == "A" or response == "a":
        time.sleep(3)
        print("After crossing the bridge, you have no way to stop him chasing you.")
        time.sleep(4)
        print("As he catches up, you accept fate.")
        time.sleep(3.5)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        time.sleep(3)
        print("You cut the rope and the bridge falls in the river, along with the monster.")
        time.sleep(4)
        print("It gets swept away by the current and you are able to escape and get home. YOU WIN!")
    else:
        print("Invalid response")
        sling_knife_run_half()

def knife_bat_run():
    time.sleep(3)
    print("You come across a draw bridge. The monster is still running after you.")
    time.sleep(2.5)
    response = input("After crossing the bridge do you: A) Continue running B) Cut the ropes on the bridge? ")
    if response == "A" or response == "a":
        time.sleep(3)
        print("After crossing the bridge, you have no way to stop him chasing you.")
        time.sleep(4)
        print("As he catches up, you accept fate.")
        time.sleep(3.5)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        time.sleep(3)
        print("You cut the rope and the bridge falls in the river, along with the monster.")
        time.sleep(4)
        print("It gets swept away by the current and you are able to escape and get home. YOU WIN!")
    else:
        print("Invalid response")
        knife_bat_run_half()

def sling_bat_half():
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You decide to run and come across a draw bridge. The monster is still running after you!")
        time.sleep(4.5)
        print("After crossing the bridge, you have no way to stop him chasing you,")
        time.sleep(3.5)
        print("as he catches up you accept fate, IT'S CLAWS COME DOWN!")
        time.sleep(3)
        print("GAME OVER!")
    elif response == "B" or response == "b":
        print("You combine the slingshot and the batteries and fire it at the monster. . .")
        time.sleep(5)
        print("YOU HIT!")
        time.sleep(2)
        print("The creature is stunned and you are able to run away.")
        time.sleep(3)
        print("As you're running you come across a car with the keys in ignition.")
        time.sleep(4)
        print("You drive away to safety. YOU WIN!")
    else:
        print("Invalid response")
        sling_bat_half()

def sling_knife_half():
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You run")
        sling_knife_run()
    elif response == "B" or response == "b":
        print("You combine the slingshot and the knife but in the panic you cut the slingshot.")
        time.sleep(5)
        print("You decide to accept fate.")
        time.sleep(2)
        print("IT'S CLAWS COME DOWN! YOU DIE!")
        time.sleep(2.5)
        print("GAME OVER!" )
    else:
        print("Invalid response")
        sling_knife_half()

def knife_bat_half():
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You run")
        knife_bat_run()
    elif response == "B" or response == "b":
        print("You stab the battery with the knife and it EXPLODES!")
        time.sleep(4)
        print("'Well, that was useless.'")
        time.sleep(2)
        print("You decide to accept fate.")
        time.sleep(2)
        print("IT'S CLAWS COME DOWN! YOU DIE!")
        time.sleep(2)
        print("GAME OVER!" )
    else:
        print("Invalid response")
        knife_bat_half()

def sling_bat():
    time.sleep(3)
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You decide to run and come across a draw bridge. The monster is still running after you!")
        time.sleep(4.5)
        print("After crossing the bridge, you have no way to stop him chasing you,")
        time.sleep(3.5)
        print("as he catches up you accept fate, IT'S CLAWS COME DOWN!")
        time.sleep(3)
        print("GAME OVER!")
    elif response == "B" or response == "b":
        print("You combine the slingshot and the batteries and fire it at the monster. . .")
        time.sleep(5)
        print("YOU HIT!")
        time.sleep(2)
        print("The creature is stunned and you are able to run away.")
        time.sleep(3)
        print("As you're running you come across a car with the keys in ignition.")
        time.sleep(3)
        print("You drive away to safety. YOU WIN!")
    else:
        print("Invalid response")
        sling_bat_half()

def sling_knife():
    time.sleep(3)
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You run")
        sling_knife_run()
    elif response == "B" or response == "b":
        print("You combine the slingshot and the knife but in the panic you cut the slingshot.")
        time.sleep(5)
        print("You decide to accept fate.")
        time.sleep(2)
        print("IT'S CLAWS COME DOWN! YOU DIE!")
        time.sleep(2.5)
        print("GAME OVER!" )
    else:
        print("Invalid response")
        sling_knife_half()

def knife_bat():
    time.sleep(3)
    response = input("Being faced with the monster you have two options. A) Run! B) Combine your two items ")
    if response == "A" or response == "a":
        print("You run")
        knife_bat_run()
    elif response == "B" or response == "b":
        print("You stab the battery with the knife and it EXPLODES!")
        time.sleep(4)
        print("'Well, that was useless.'")
        time.sleep(2)
        print("You decide to accept fate.")
        time.sleep(2)
        print("IT'S CLAWS COME DOWN! YOU DIE!")
        time.sleep(2)
        print("GAME OVER!" )
    else:
        print("Invalid response")


def path_2_bag_half():
    response = input("Which do you pick? A) Knife & Batteries B) Slingshot & Knife C) Slingshot & Batteries ")
    if response == "A" or response == "a":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        knife_bat()
    elif response == "B" or response == "b":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        sling_knife()
    elif response == "C" or response == "c":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        sling_bat()
    else:
        print("Invalid response")
        path_2_bag_half()

def path_2_bag():
    print("You search the bag and find: a hunter's slingshot, batteries and a flip knife.")
    time.sleep(2.5)
    response = input("You can only hold 2 items, which do you pick? A) Knife & Batteries B) Slingshot & Knife C) Slingshot & Batteries ")
    if response == "A" or response == "a":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        knife_bat()
    elif response == "B" or response == "b":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        sling_knife()
    elif response == "C" or response == "c":
        print("After choosing your two items, you continue down the path.")
        time.sleep(3)
        print("You hear the noise of passing cars. Relief washes over you as you run towards the noise in hopes of getting a lift home.")
        time.sleep(5)
        print("Suddenly you hear footsteps. You stop, wondering where it's coming from.")
        time.sleep(4)
        print("The sound of cars completely stops. That ever so familiar gagging smell!!!")
        time.sleep(4)
        print("You shine the torch up, what you think is a tree, it's no tree. . .")
        time.sleep(3)
        print("It is a vile, crusty creature with a head that looks like a speaker! You realise all along this is the creature that has been mimicking the noise!")
        time.sleep(5)
        sling_bat()
    else:
        print("Invalid response")
        path_2_bag_half()

def path_2_forf_half():
    response = input("What do you do? A) FIGHT! B) Flight ")
    if response == "A" or response == "a": 
        print("You chose to fight. All you have on you is a torch.")
        time.sleep(3)
        print("You throw it at the monster's head...")
        time.sleep(3)
        print("Of course it does nothing. You decide to accept fate.")
        time.sleep(3)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        print("You decide to flee and escape before the monster can get you.")
        time.sleep(4)
        print("After running for some time, you stumble upon a broken bag. ")
        time.sleep(3)
        path_2_bag()
    else:
        print("Invalid response")
        path_2_forf_half()

def path_2_forf():
    response = input("Fight or flight sets in. What do you do? A) FIGHT! B) Flight ")
    if response == "A" or response == "a": 
        print("You chose to fight. All you have on you is a torch.")
        time.sleep(3)
        print("You throw it at the monster's head...")
        time.sleep(3)
        print("Of course it does nothing. You decide to accept fate.")
        time.sleep(3)
        print("IT'S CLAWS COME DOWN! GAME OVER! ")
    elif response == "B" or response == "b":
        print("You decide to flee and escape before the monster can get you.")
        time.sleep(3)
        print("After running for some time, you stumble upon a broken bag. ")
        time.sleep(3)
        path_2_bag()
    else:
        print("Invalid response")
        path_2_forf_half()

def path_1_mother_half():
    response = input("Pick a path: A) Path one B) Path two ")
    if response == "A" or response == "a":
        print("You come to a dark creepy cabin and decide to venture in.")
        time.sleep(3)
        print("As you slowly open the door, it creaks. What you see shocks and disgusts you")
        time.sleep(5.5)
        print("'IT'S JAY!' you exclaim! He's sitting there in the cabin playing scary games on his PS4. Phew!!! You decide to stay and play games.")
        time.sleep(3.5)
        print("Game End.")
    elif response == "B" or response == "b":
        print("The crying is geting louder, almost deafening, as your eyes dart around hoping to find your mother. The now familiar gagging smell, so close.")
        time.sleep(5)
        print("In the near distance, camouflaged among the branches, a shadow becomes clearer.")
        time.sleep(4)
        print("Now you can see some tall disgusting, mummified looking monster running towards you. ")
        time.sleep(5)
        path_2_forf()
    else:
        print("Invalid response")
        path_1_mother_half()
        
def path_1_mother():
    time.sleep(3)
    print("You continue to walk.")
    time.sleep(3)
    print("'That is definitely my mother. Why is she upset?'")
    time.sleep(3)
    response = input("There are two paths but you hear her down both. Pick a path: A) Path one B) Path two ")
    if response == "A" or response == "a":
        print("You come to a dark creepy cabin and decide to venture in.")
        time.sleep(3)
        print("As you slowly open the door, it creaks. What you see shocks and disgusts you.")
        time.sleep(5.5)
        print("'IT'S JAY!' you exclaim! He's sitting there in the cabin playing scary games on his PS4. Phew!!! You decide to stay and play games.")
        time.sleep(3)
        print("Game End.")
    elif response == "B" or response == "b":        
        print("The crying is getting louder, almost deafening, as your eyes dart around hoping to find your mother. The now familiar gagging smell, so close.")
        time.sleep(5)
        print("In the near distance, camouflaged among the branches, a shadow becomes clearer.")
        time.sleep(4)
        print("Now you can see some tall disgusting, mummified looking monster running towards you. ")
        time.sleep(5)
        path_2_forf()
    else:
        print("Invalid response")
        path_1_mother_half()


def level_three_path_half():
    response = input("Pick a path: A) Left B) Right ")
    if response == "A" or response == "a":
        print("This looks like the correct path…")
        time.sleep(3)
        print("You hear a voice in the distance, a familiar voice...")
        time.sleep(3)
        print("'Is that my mother??' ")
        time.sleep(2)
        path_1_mother()
    elif response == "B" or response == "b":
        print("You go right and stumble upon a broken bag.")
        time.sleep(2)
        path_2_bag()
    else:
        print("Invalid response.")
        level_three_path_half()

def level_three():
    time.sleep(1)
    print("The stench in the damp air seems to get heavier. 'What's that smell???' ")
    time.sleep(3.5)
    response = input("You look down the paths, they look exactly the same. Pick a path: A) Left B) Right ")
    if response == "A" or response == "a":
        print("This looks like the correct path…")
        time.sleep(3)
        print("You hear a voice in the distance, a familiar voice...")
        time.sleep(4)
        print("'Is that my mother??' ")
        time.sleep(2)
        path_1_mother()
    elif response == "B" or response == "b":
        print("You go right and stumble upon a broken bag. ")
        time.sleep(2)
        path_2_bag()
    else:
        print("Invalid response.")
        level_three_path_half()
        
def stuck_in_forest():
    response = input("Make up your mind! Do you want to A) Pick up torch? B) Leave it and go back? ") 
    if response == "A" or response ==  "a":
        print("You pick up the torch and turn it on. Now you can see two dirt paths clearly.")
        time.sleep(3)
        level_three()
    elif response == "B" or response == "b":
        print("Leaving so soon?")
        time.sleep(2)
        level_one()
    else:
        time.sleep(2)
        print("Invalid response.")
        stuck_in_forest()

def level_two():
    time.sleep(2.5)
    print("You stumble on, going deeper into the forest, so aware of how dark and creepy it feels, the wet leaves and branches slapping against your face whilst almost gagging from the unfamiliar stench. ")
    time.sleep(5)
    print("In the distance a faint light beckons, you stumble over a branch, no it can't be...")
    time.sleep(4)
    print("Yes, it's a torch! It works! ")
    time.sleep(2.5)
    response = input("Do you want to: A) Pick up torch? B) Leave it and go back? ") 
    if response == "A" or response ==  "a":
        print("You pick up the torch and turn it on. Now you can see two dirt paths clearly. ")
        time.sleep(3)
        level_three()
    elif response == "B" or response == "b":
        print("Leaving so soon?")
        time.sleep(2)
        stuck_in_forest()
    else:
        print("Invalid response.")
        time.sleep(2)
        stuck_in_forest()

def correct_name():
    time.sleep(2)
    name = input("Please enter your correct name: ")
    time.sleep(2)
    response = input("Are you sure? Yes or No. ")
    time.sleep(2)
    if response == "yes" or response == "Yes" or response == "y" or response == "Y":
        print("Hello, {}".format(name))
        level_one()
    elif response == "no" or response == "No" or response == "n" or response == "N":
        print("Come on now, who spells their name wrong this many times!? ")
        correct_name()

def level_one_half():
        response = input ("Which way will you go? A) Forward B) Left C) Right D) Back. ")
        if response == "A" or response == "a":
            time.sleep(2.5)
            print("The path is clear and you wearily walk forward.")
            time.sleep(2)
            level_two()
        elif response == "B" or response == "b":
            print("You can't go this way the bushes are too thick and spikey.")
            time.sleep(2)
            level_one_half()
        elif response == "C" or response == "c":
            print("You can't go this way the bushes are too thick and spikey.")
            time.sleep(2)
            level_one_half()
        elif response == "D" or response == "d":
            print("You hit a tree there is nowhere to go.")
            time.sleep(2)
            level_one_half()
        else:
            print("Invalid response.")
            level_one_half()
            
def level_one():
    time.sleep(2)
    print("It's a foggy, damp and frosty night in the forest. ")
    time.sleep(3)
    print("Branches hung like life sized over bearing arms. ")
    time.sleep(3)
    print("The eerie silence of the night, with the occasional hooting of the night owls made for uncomfortable company. ")
    time.sleep(4)
    print("You felt as if you were being watched by the unknown lurking in the shadows.")
    time.sleep(3)
    print("Although you were in a place of solitude, you felt a million eyes watching. ")
    time.sleep(3)
    print("You have just woken up to find you are all alone. ")
    time.sleep(3)
    print("The camp fire is out. 'oh dear!! I must have overslept!! Everyone is gone!! I need to leave now!!!' ")
    time.sleep(3)
    response = input ("Which way will you go? A) Forward B) Left C) Right D) Back. ")
    if response == "A" or response == "a":
        time.sleep(2.5)
        print("The path is clear and you wearily walk forward.")
        time.sleep(2)
        level_two()
    elif response == "B" or response == "b":
        print("You can't go this way the bushes are too thick and spikey.")
        time.sleep(2)
        level_one_half()
    elif response == "C" or response == "c":
        print("You can't go this way the bushes are too thick and spikey.")
        time.sleep(2)
        level_one_half()
    elif response == "D" or response == "d":
        print("You hit a tree there is nowhere to go.")
        time.sleep(2)
        level_one_half()
    else:
        print("Invalid response.")
        time.sleep(2)
        level_one_half()

def start_game():
    print("Hello and welcome to 'The Siren'. Throughout the game you will be faced with obstacles, you will be required to respond with a letter corresponding with the option you want to select.")
    time.sleep(2.5)
    global name
    name = input("What is your name? ")
    time.sleep(1)
    response = input ("Is {} correct? Yes or No ".format(name))
    if response == "yes" or response == "Yes" or response == "y" or response == "Y":
        time.sleep(1)
        print("Hello, {}".format(name))
        level_one()
    elif response == "no" or response == "No" or response == "n" or response == "N":
        correct_name()
        start_game()
start_game()