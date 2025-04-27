from database import ExpenseDatabase

db = ExpenseDatabase()

# Добавить расход:
db.add_expense("Кофе", 250)

# Получить все расходы:
expenses = db.get_all_expenses()
for expense in expenses:
    print(expense)

# Получить сумму всех расходов:
total = db.get_total_amount()
print("Общая сумма:", total)

db.close()
