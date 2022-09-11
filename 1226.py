from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):  
        self.locks[philosopher - (philosopher % 2)].acquire()
        self.locks[philosopher - (not philosopher % 2)].acquire()
        
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        
        self.locks[philosopher - (philosopher & 1)].release()
        self.locks[philosopher - (~philosopher & 1)].release()