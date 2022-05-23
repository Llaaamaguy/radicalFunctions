from radfunc import Function
import matplotlib.pyplot as plt
from tabulate import tabulate
import os
from inputParser import parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--graphto", help="Where to graph to", type=int, default=10)
parser.add_argument("--show_points", default=False, type=bool)
args = parser.parse_args()


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear()
    while True:
        user_input = input("Enter function: ")
        if user_input == "quit":
            break
        func = parse(user_input, args.graphto)

        points = func.graph()

        if args.show_points:
            printPoints = [[points[0][i], points[1][i]] for i in range(len(list(points[0])))]
            print(tabulate(printPoints, headers=["X", "Y"], tablefmt="grid"))

        if points[0][0] < 0:
            fig = plt.figure()
            myplot = fig.add_subplot()
            myplot.plot(points[0], points[1])
            myplot.spines.left.set_position("center")
            myplot.spines.right.set_color("none")
            myplot.spines.bottom.set_position('center')
            myplot.spines.top.set_color('none')
            myplot.xaxis.set_ticks_position('bottom')
            myplot.yaxis.set_ticks_position('left')
            plt.title(str(func))
        else:
            plt.plot(points[0], points[1])

        plt.show()
        clear()


if __name__ == "__main__":
    main()
