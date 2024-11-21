class Memory:
    def __init__(self):
        self.value = 0

    def Add(self, value):
        self.value += value
        return self.value

    def Subtract(self, value):
        self.value -= value
        return self.value

    def Clear(self):
        self.value = 0
        return self.value

    def Read(self):
        return self.value
