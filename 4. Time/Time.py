
class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    
    def display(self):
        print(f"{self.h}h {self.m}min")

    def add(self, h, m):
        self.h = (self.h + h) % 24 + (self.m + m) // 60
        self.m = (self.m + m) % 60
    
def createTime(time:Time, h:int, m:int):
    new_time = Time(time.h, time.m)
    new_time.add(h, m)
    return new_time

# time = Time(12, 0)
# time.display()
# time.add(6, 30)
# time.display()
# time.add(0, 50)
# time.display()

# print(" . . . ")

# new = createTime(time, 1, 5)
# new.display()