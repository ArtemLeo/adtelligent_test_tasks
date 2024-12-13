import json
import pandas as pd

# Вказуємо шлях до JSON-файлу
json_file_path = "data.json"

# Завантаження JSON-даних із файлу
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Перетворення даних у DataFrame
df = pd.DataFrame(data)

# Розрахунок ключових показників
total_quantity = df['quantity'].sum()
total_sales = df['sales'].sum()

print(f"Загальна кількість проданих одиниць: {total_quantity}")
print(f"Загальна сума продажів: ${total_sales}")

# Збереження даних у Excel
df.to_excel("sales_report.xlsx", index=False)
print("Дані збережено у файл sales_report.xlsx")