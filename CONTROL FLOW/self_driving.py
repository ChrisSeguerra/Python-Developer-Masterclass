# SELF DRIVING 

destination = input("Where do you want to go? ")



def start_engine():
    print("Starting engine...")

def move_forward():
    print("Moving forward")

def turn(direction):
    print(f"Turning {direction}")

def stop_engine():
    print("Stopping!")


start_engine()
move_forward()

if destination == "school":
    turn("right")
    print("We arrived at the school.")


elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("right")
        print("We arrived at the gorcery store!")
    else:
        turn("left")
        print("We arrived at the dentist.")


elif destination == "restaurant":
    move_forward()
    print("We arrived at the restaurant.")


else:
    print("Invalid destination")