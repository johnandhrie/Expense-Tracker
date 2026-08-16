budget = 0
transpo = 0
util = 0
insurance = 0
food = 0

def Add(budget, transpo, util, insurance, food):
    budget = int(input("Add Budget: "))
    transpo = int(input("Transportation expense (Gas and travel expense): "))
    util = int(input("Utilities expense (Subscription, Bills, etc.): "))
    insurance = int(input("Insurance expense (Car insurance, Health insurance, etc.): "))
    food = int(input("Food expense (i.e. Groceries): "))

    return budget, transpo, util, insurance, food