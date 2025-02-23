from collections import deque

class WaterJugAgent:
    def _init_(self, capacity1, capacity2, goal):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.goal = goal
        self.visited = set()

    def bfs(self):
        initial_state = (0, 0)
        queue = deque([(initial_state, [])])  # (state, path)
        self.visited.add(initial_state)

        while queue:
            (jug1, jug2), path = queue.popleft()

            if jug1 == self.goal or jug2 == self.goal:
                print("Goal achieved! Path:", path + [(jug1, jug2)])
                return

            # List of all possible next states
            next_states = [
                (self.capacity1, jug2), 
                (jug1, self.capacity2),  
                (0, jug2),             
                (jug1, 0),              
                (max(0, jug1 - (self.capacity2 - jug2)), min(self.capacity2, jug2 + jug1)), 
                (min(self.capacity1, jug1 + jug2), max(0, jug2 - (self.capacity1 - jug1)))  
            ]
            
            # Add new states to the queue
            for state in next_states:
                if state not in self.visited:
                    self.visited.add(state)
                    queue.append((state, path + [(jug1, jug2)]))

        print("No solution found.")

agent = WaterJugAgent(3, 5, 4)
agent.bfs()