# //In our monthly expense example, print monthly no.
# // and expense and then in the end print total expense

expense = [2340, 2500, 2100, 3020, 2980, 3990]
total = 0
# for i in range(len(expanse)):
for i in range(6):
    print('Month:', (i+1), 'Expense:', expense[i])
    total = total + expense[i]
    print("Total expense is: ", total)
