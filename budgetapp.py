from budgetfuncs import Budget

food = Budget(200)
food.deposit(20)
food.withdraw(50)

bills = Budget(800)
bills.deposit(200)
bills.withdraw(500)

food.deposit(bills.withdraw(100))
