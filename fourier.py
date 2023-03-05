from calculus import *
import math

class FourierSeries:
    def _a(f, j:int):
        return simpsons_rule(lambda t: f(t)*math.cos(j*t), -math.pi, math.pi) / math.pi
    def _b(f, j:int): 
        return simpsons_rule(lambda t: f(t)*math.sin(j*t), -math.pi, math.pi) / math.pi

    def __init__(self, f, n:int):
        self.n = n
        self._ab = [(FourierSeries._a(f, j), FourierSeries._b(f, j)) for j in range(n)]
    
    def eval(self, t:float)->float:
        total = 0
        for j in range(1, self.n):
            a, b = self._ab[j]
            total += a*math.cos(j*t) + b*math.sin(j*t)
        # not adding a0 puts the series series too low
        return total + self._ab[0][0]/2