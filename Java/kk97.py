class car:
    def __init__(self):
        self.acc = False
        self.brk = False
    def start(self):
        self.acc = True
        print("car started")
        
s1 = car()
s1.start()