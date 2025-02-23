class ReflexAgent:
    def _init_(self):
        self.rooms = {"A": False, "B": False, "C": False, "D": False}
        self.room_order = ["A", "B", "C", "D"]  # Order of rooms
        self.current_room = "A"  # Start in Room A

    def sense_environment(self):
        # Check if the current room is dirty
        return not self.rooms[self.current_room]

    def clean_room(self):
        print(f"Cleaning Room {self.current_room}")
        self.rooms[self.current_room] = True
        self.print_rooms_status()

    def move_to_next_room(self):
        current_index = self.room_order.index(self.current_room)
        next_index = (current_index + 1) % len(self.room_order)
        self.current_room = self.room_order[next_index]
        print(f"Moving to Room {self.current_room}")

    def print_rooms_status(self):
        print("Room Status:")
        for room, status in self.rooms.items():
            status_text = "Clean" if status else "Dirty"
            print(f"  Room {room}: {status_text}")
        print()

    def perform_cleaning(self):
        while not all(self.rooms.values()):
            if self.sense_environment():
                self.clean_room()
            self.move_to_next_room()
        print("All rooms are cleaned!")

def main():
    agent = ReflexAgent()
    agent.perform_cleaning()


if _name_ == "_main_":
    main()