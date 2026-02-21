# Monkey Banana Problem - Simple Simulation

class State:
    def __init__(self, monkey_pos, box_pos, on_box, has_banana):
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.on_box = on_box
        self.has_banana = has_banana

def monkey_banana():
    # Initial State
    state = State("A", "B", False, False)
    banana_pos = "C"

    print("Initial State:")
    print(state.__dict__)

    # Step 1: Monkey walks to box
    print("\nMonkey walks to the box.")
    state.monkey_pos = state.box_pos

    # Step 2: Monkey pushes box under banana
    print("Monkey pushes the box to the banana position.")
    state.box_pos = banana_pos
    state.monkey_pos = banana_pos

    # Step 3: Monkey climbs the box
    print("Monkey climbs onto the box.")
    state.on_box = True

    # Step 4: Monkey grabs banana
    if state.on_box and state.monkey_pos == banana_pos:
        print("Monkey grabs the banana!")
        state.has_banana = True

    print("\nGoal State Reached:")
    print(state.__dict__)

monkey_banana()
