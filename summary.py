def Summary(budget, transpo, util, insurance, food, total_expenses):
    remaining = budget - total_expenses

    print("\n========== EXPENSE SUMMARY ==========")
    print("Budget:             ", budget)
    print("Transportation:     ", transpo)
    print("Utilities:          ", util)
    print("Insurance:          ", insurance)
    print("Food:               ", food)
    print("--------------------------------------")
    print("Total Expenses:     ", total_expenses)
    print("Remaining Budget:   ", remaining)
    print("======================================")