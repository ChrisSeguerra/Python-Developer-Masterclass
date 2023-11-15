# Navigating the Self-Driving Car through Complex City

roundabout_exits = {
    1: "hospital",
    2: "mall",
    3: "airport",
    4: "university"
}


def move_forward():
    print("Moving forward")

def turn(direction):
    print(f"Turning {direction}")

def start_engine(): 
    print("Starting engine...")

def stop_engine():
    print("Stopping engine...")

def follow_roundabout(exit_number):
    if exit_number in roundabout_exits:
        print(f"Taking exit number {exit_number} from the roundabout.")


start_engine()


destination = input("Where do you want to go? ")
if destination == "library":
    move_forward()
    turn("left")
    print(f"We arrived at the {destination}.")
    stop_engine()

elif destination == "tech park":
    move_forward()
    turn("right")
    print(f"We arrived at the {destination}.")
    stop_engine()
     
elif destination == "hospital":
    move_forward()
    print("Entering the roundabout...")
    follow_roundabout(1)
    move_forward()
    print(f"We arrived at the {destination}.")
    stop_engine()

elif destination == "mall":
    move_forward()
    print("Entering the roundabout...")
    follow_roundabout(2)
    move_forward()
    turn("right")
    print(f"We arrived at the {destination}.")
    stop_engine()

elif destination == "airport":
    move_forward()
    print("Entering the roundabout...")
    follow_roundabout(3)
    move_forward()
    print(f"We arrived at the {destination}.")
    stop_engine()

elif destination == "university" or destination == "stadium":
    move_forward()
    print("Entering the roundabout...")
    follow_roundabout(4)
    move_forward()
    if destination == "university":
        turn("left")
        print(f"We arrived at the {destination}.")
        stop_engine()
    if destination == "stadium":
        turn("right")
        print(f"We arrived at the {destination}.")
        stop_engine()
else:
    print("Invalid destination")
    