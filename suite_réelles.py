from compose import Compose

class SuiteRéelles:
    def __init__(self,equation):
        self.equation = equation
    def calc(self):
        eq = Compose(self.equation)
        print(eq.start())
