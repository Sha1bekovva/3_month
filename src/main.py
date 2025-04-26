import flet as ft

def main(page: ft.Page):
    page.title = "Учёт расходов"

    expenses = []  # Список для хранения всех расходов
    total_amount = 0  # Общая сумма

    # Колонка для отображения списка расходов
    expenses_list = ft.Column()
    # Текст для отображения общей суммы
    total_text = ft.Text("Общая сумма: 0 сом")

    def add_expense(e):
        nonlocal total_amount  # Чтобы менять переменную снаружи

        description = desc_input.value.strip()
        amount_str = amount_input.value.strip()

        # Проверяем, что сумма является числом и положительным
        if description and amount_str.replace(".", "", 1).isdigit():
            amount = float(amount_str)

            if amount > 0:  # Если сумма положительная
                expenses.append({"desc": description, "amount": amount})

                # Определяем цвет в зависимости от суммы
                if amount <= 100:
                    color = ft.Colors.GREEN
                elif amount <= 1000:
                    color = ft.Colors.PINK
                elif amount <= 10000:
                    color = ft.Colors.RED
                else:
                    color = ft.Colors.PURPLE

                # Обновляем визуальный список с нужным цветом
                expenses_list.controls.append(
                    ft.Text(f"{description} — {amount} сом", color=color)
                )

                # Обновляем общую сумму
                total_amount += amount
                total_text.value = f"Общая сумма: {total_amount} сом"

                # Очищаем поля ввода
                desc_input.value = ""
                amount_input.value = ""
                page.update()
            else:
                print("Сумма должна быть положительным числом.")
        else:
            print("Введите корректную сумму (например: 1250).")

    # Поля ввода
    desc_input = ft.TextField(label="На что потрачено?")
    amount_input = ft.TextField(label="Сколько?", keyboard_type=ft.KeyboardType.NUMBER)

    # Кнопка
    add_button = ft.ElevatedButton(text="Добавить расход", on_click=add_expense)

    # Добавляем всё на страницу
    page.add(desc_input, amount_input, add_button, expenses_list, total_text)

ft.app(target=main)
