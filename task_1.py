from pulp import LpMaximize, LpProblem, LpVariable, value

# Створення моделі задачі
model = LpProblem(name="maximize-drinks", sense=LpMaximize)

# Змінні: кількість лимонаду (L) і фруктового соку (F)
L = LpVariable(name="lemonade", lowBound=0, cat="Integer")
F = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Обмеження на ресурси
model += (2 * L + 1 * F <= 100, "Water_constraint")
model += (1 * L <= 50, "Sugar_constraint")
model += (1 * L <= 30, "Lemon_juice_constraint")
model += (2 * F <= 40, "Fruit_puree_constraint")

# Цільова функція: максимізувати сумарну кількість продуктів
model += L + F

# Розв'язання задачі
model.solve()

# Результати
print(f"Кількість лимонаду: {L.value()}")
print(f"Кількість фруктового соку: {F.value()}")
print(f"Загальна кількість вироблених одиниць: {value(model.objective)}")

