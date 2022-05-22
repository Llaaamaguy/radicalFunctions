from radfunc import Function
import matplotlib.pyplot as plt
from tabulate import tabulate

func = Function("x", index=3, co1=-3)
print(func)

points = func.graph()

printPoints = [[points[0][i], points[1][i]] for i in range(len(list(points[0])))]

print(tabulate(printPoints, headers=["X", "Y"], tablefmt="grid"))


fig = plt.figure()
myplot = fig.add_subplot()
myplot.plot(points[0], points[1])
myplot.spines.left.set_position("center")
myplot.spines.right.set_color("none")
myplot.spines.bottom.set_position('center')
myplot.spines.top.set_color('none')
myplot.xaxis.set_ticks_position('bottom')
myplot.yaxis.set_ticks_position('left')

plt.show()
