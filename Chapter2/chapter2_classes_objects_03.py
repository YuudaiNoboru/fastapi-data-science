class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
    
    def __repr__(self):
        return f"Temperature({self.value},{self.scale!r})"
    def __str__(self):
        return f"Temperature is {self.value} °{self.scale}"

t = Temperature(20, "C")
print(repr(t))
print(str(t))
print(t)
    