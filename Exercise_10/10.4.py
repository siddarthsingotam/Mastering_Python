import random

# Car class defined.
class Car:
    def __init__(self, reg_no="Not selected", cur_spd=0, max_spd=0, dist=0):
        self.reg_no = reg_no
        self.max_spd = max_spd
        self.cur_spd = cur_spd
        self.dist = dist

    def accelerate(self, change_of_speed):
        self.cur_spd = self.cur_spd + change_of_speed
        if self.cur_spd >= self.max_spd:
            self.cur_spd = self.max_spd
        elif self.cur_spd <= 0:
            self.cur_spd = 0
        return self.cur_spd

    def drive(self, drive):   # here drive is the time of travel
        self.dist = self.dist + self.cur_spd*drive
        return self.dist


class Race:

    def __init__(self, name, distance, carxlist):
        self.name = name
        self.distance = distance
        self.carxlist = carxlist

    def hour_passes(self):
        for car in self.carxlist:
            self.carxlist[car.cur_spd].accelerate(random.randint(-10, 15))
            self.carxlist[car.dist].drive(1)

    def print_status(self):
        for car in self.carxlist:
            print(
                f"Car: {car.reg_no}, Current speed: {car.cur_spd}, Max speed: {car.max_spd}, Distance: {car.dist}")

    def race_finished(self):
        race_over = False
        while not race_over:
            self.hour_passes()
            for car in self.carxlist:
                if car.dist >= self.distance:
                    race_over = True

# Adding car objects in a list using a for loop
car_list = []
total_cars_in_game = 10
for i in range(total_cars_in_game):
    max_spd = random.randint(100, 200)
    reg_no = "ABC-" + str(i + 1)
    car_list.append(Car(reg_no, max_spd=max_spd))


# Main Program

super_cars = Race("Grand Demolition Derby", 8000, car_list)

while True:
    super_cars.hour_passes()
    super_cars.print_status()
    if super_cars.race_finished():
        break

#for car in self.carxlist:
    #race_over = False
    #while not race_over:
        #if car.distance >= self.distance:
            #race_over = True

























































