class Greetings:
    def __init__(self):
        pass

    def greet(self, name="guest", message="welcome"):
        print(f"Welcome {name}, {message}")


obj = Greetings()
obj.greet("Pritam")




class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add())            # 0
print(calc.add(5))           # 5
print(calc.add(5, 10))       # 15
print(calc.add(5, 10, 20))   # 35




class Calculator:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total


calc = Calculator()

print(calc.add())                 # 0 (no arguments)
print(calc.add(5))                # 5 (one argument)
print(calc.add(5, 10))            # 15 (two arguments)
print(calc.add(5, 10, 20))        # 35 (three arguments)
print(calc.add(1, 2, 3, 4, 5))    # 15 (five arguments)
