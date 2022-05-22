import numpy as np
from exprParser import eval_expr
import collections


class Function:
    def __init__(self, radicand, index=2, co1=1, co2=0, graphto=10):
        self.index = int(index)
        self.radicand = radicand
        self.co1 = int(co1)
        self.co2 = int(co2)
        self.graphto = graphto
        self.op2 = "+" if self.co2 >= 1 else "-"
        self.special_chars = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "rad": "√"}

    def __super_str(self, string):
        return "".join([self.special_chars[i] for i in str(string)])

    def __repr__(self):
        return f"{str(self.co1)} * {self.__super_str(self.index)}{self.special_chars['rad']}({self.radicand}) {self.op2} {abs(self.co2)}"

    def graph(self):
        points = {}
        for i in range(self.graphto):
            x = i
            new_radicand = self.radicand.replace("x", str(x))
            new_radicand = eval_expr(new_radicand)
            after_rad = new_radicand**(1/self.index)
            new_expr = f"{self.co1}*{after_rad}{self.op2}{self.co2}"
            y = eval_expr(new_expr)
            x_toAdd = [x]
            y_toAdd = [y] if y != -0 else [0]
            if self.index % 2 != 0 and y != 0:
                x_toAdd.append(-x)
                y_toAdd.append(-y)
            for i in range(len(x_toAdd)):
                points[x_toAdd[i]] = y_toAdd[i]

        ordered = dict(sorted(points.items()))
        points = [np.array(list(ordered.keys())), np.array(list(ordered.values()))]
        return points

