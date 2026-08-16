from add_expense import Add
from Calculate import Calculate
from summary import Summary

def main():

    budget = 0
    transpo = 0
    util = 0
    insurance = 0
    food = 0

    budget, transpo, util, insurance, food = Add(
        budget,
        transpo,
        util,
        insurance,
        food
    )

    total_expenses = Calculate(
        transpo,
        util,
        insurance,
        food
    )

    Summary(
        budget,
        transpo,
        util,
        insurance,
        food,
        total_expenses
    )

if __name__ == "__main__":
    main()