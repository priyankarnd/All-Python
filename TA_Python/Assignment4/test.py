def InvestGoal(investment, goal):
    """This function will calculate how long it will take to reach the goal"""

    years = 0

    while investment <= goal:
        investment = (investment * .08) + investment
        years += 1

    return "it will take approximately " + str(years) + " years to reach your investment goal"


InvestGoal(10000, 1000000)