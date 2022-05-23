from radfunc import Function
from exprParser import eval_expr


def parse(user_input, graphto):
    split = user_input.split(" ")

    co1 = split[0]
    if co1[0] == "(" and co1[-1] == ")":
        co1 = eval_expr(co1.split(")")[1].split("(")[1])
    else:
        co1 = int(co1)

    rad = split[1].split("rad")
    index = rad[0]
    radicand = rad[-1]

    co2 = split[-1]
    if co2[0] == "(" and co2[-1] == ")":
        co2 = eval_expr(co2.split(")")[1].split("(")[1])
    else:
        co2 = int(co2)

    return Function(radicand, index=index, co1=co1, co2=co2, graphto=graphto)
