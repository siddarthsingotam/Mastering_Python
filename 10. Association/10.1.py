class Elevator:
    def __init__(self, top_floor, bottom_floor=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.cur_floor = bottom_floor

    def floor_up(self): # Method to go UP⬆⬆️⬆️️
        self.cur_floor = self.cur_floor + 1

    def floor_down(self): # Method to go DOWN⬇⬇️⬇️️
        self.cur_floor = self.cur_floor - 1

    def go_to_floor(self, floor): # Method to destination floor.📌📌📌
        if floor == self.cur_floor:
            print(f"Present on floor: {self.cur_floor}. Moving elvator to bottom floor: {self.bottom_floor}")

        while floor != self.cur_floor and self.bottom_floor <= floor <= self.top_floor:
            if floor > self.cur_floor:
                self.floor_up()
                print(f"Going up, now on floor: {self.cur_floor}")

            if floor < self.cur_floor:
                self.floor_down()
                print(f"Going down, now on floor: {self.cur_floor}")
        print(f"Reached floor: {self.cur_floor} and moving to bottom floor: {self.bottom_floor} ")


# Main Program
h = Elevator(10) # 10 floors
print("Lift going UP")
# testing floor up ⬆️⬆️⬆️
h.cur_floor = 3 # current floor
h.go_to_floor(9)

print(f"\nLift going DOWN")

# testing floor down ⬇️⬇️⬇️
h.cur_floor = 9 # current floor
h.go_to_floor(3)
