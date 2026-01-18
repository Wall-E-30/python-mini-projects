name = input("What would you like to be called as: ")
print("Let's start our journey,", name,"!!")

response = input("You were on a path and it has come to an end, choose your direction. You can choose either port beam or starboard beam.\n").lower()

if response == "port beam":
    response = input("You reached a port, would you like to explore the port or move ahead to another one? Type 'explore' or 'another'").lower()

    if response == "explore":
        print(name,"started exploration.")
    
    elif response == "another":
        print(name,"didn't find any other port.\nYou lose.")
    
    else:
        print("You didn't chose, wave hit the boat.\nYou lose.")

elif response == "starboard beam":
    print("Weather is bad!!!")

    response = input("Get inside or sail across??\n").lower()

    if response == "get inside":
        print(name ,"rested till the weather was clear.")

    elif response == "sail across":
        print("A big wave hit the ship!\nYou lose.")

    else:
        print("You didn't make any decision.\nYou lose.")

else:
    print("You took too much time to choose.\nYou lose.")