from random import choice


class Randomwalk:
    def __init__(self,total_walk=5000):
        self.total_walk=total_walk
        self.x_place=[0]
        self.y_place=[0]
        self.fill_walk()
        self.get_step()

    def fill_walk(self):
        while len(self.x_place) < self.total_walk:
            x_step=self.get_step()
            y_step=self.get_step()
            if x_step==0 and y_step == 0:
                continue
            x=self.x_place[-1]+x_step
            y=self.y_place[-1]+y_step
            self.x_place.append(x)
            self.y_place.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
