
def clean_rooms(state):
    # State table (state is a list representing clean/dirty status of rooms)
    # Indexes: 0 -> Room A, 1 -> Room B, 2 -> Room C, 3 -> Room D
    # Values: True for clean, False for dirty
    room_order = ["A", "B", "C", "D"] 
    index = 0 

    while True:
        if not state[index]:
            print(f"Cleaning Room {room_order[index]}")
            state[index] = True  
            index = (index + 1) % len(state)  
            print(f"Moving to Room {room_order[index]}")  
        else:
            print("All rooms are cleaned")
            break  


def main():
    rooms = [False, False, False, False]  # All rooms are initially dirty (False)
    clean_rooms(rooms)

if _name_ == "_main_":
    main()