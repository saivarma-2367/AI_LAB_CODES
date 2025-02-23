Monkey Banana
class MonkeyBananaAgent:
    def _init_(self, grid, monkey_position, chair_position, banana_position):
        self.grid = grid
        self.monkey = monkey_position
        self.chair = chair_position
        self.banana = banana_position

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

    def update_grid(self, prev, current, symbol):
        self.grid[prev[0]][prev[1]] = '-'
        self.grid[current[0]][current[1]] = symbol

    def move(self, start, end, symbol):
        while start != end:
            prev = start
            if start[0] < end[0]:  
                start = (start[0] + 1, start[1])
            elif start[0] > end[0]: 
                start = (start[0] - 1, start[1])
            elif start[1] < end[1]:  
                start = (start[0], start[1] + 1)
            elif start[1] > end[1]:  
                start = (start[0], start[1] - 1)
            self.update_grid(prev, start, symbol)
            self.print_grid()
        return start

    def solve(self):
        print("Initial grid: ")
        self.print_grid()

        print(f"Monkey moving from {self.monkey} to the chair")
        self.monkey = self.move(self.monkey, self.chair, 'M')

        print(f"Pushing the chair from {self.chair} to the banana")
        self.chair = self.move(self.chair, self.banana, 'C')

        print("Monkey climbs the chair and grabs the banana!")
        print("Goal achieved!")


# Example grid setup
grid = [
    ['M', '-', '-'],  # M = Monkey
    ['-', 'C', '-'],  # C = Chair
    ['-', '-', 'B']   # B = Banana
]

agent = MonkeyBananaAgent(grid, (0, 0), (1, 1), (2, 2))
agent.solve()