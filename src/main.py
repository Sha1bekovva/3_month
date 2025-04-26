import flet as ft

def main(page: ft.Page):
    page.title = "Учёт расходов"

    expenses = []
    total_amount = 0

    # Колонка для отображения списка расходов с прокруткой
    expenses_list = ft.Column(scroll=ft.ScrollMode.AUTO)

    total_text = ft.Text("Общая сумма: 0 сом", weight=ft.FontWeight.BOLD)

    def add_expense(e):
        nonlocal total_amount

        description = desc_input.value.strip()
        amount_str = amount_input.value.strip()

        if description and amount_str.replace(".", "", 1).isdigit():
            amount = float(amount_str)

            if amount > 0:
                expenses.append({"desc": description, "amount": amount})

                # Определяем цвет суммы
                if amount <= 100:
                    amount_color = ft.Colors.GREEN
                elif amount <= 1000:
                    amount_color = ft.Colors.PINK
                elif amount <= 10000:
                    amount_color = ft.Colors.RED
                else:
                    amount_color = ft.Colors.PURPLE

                # Добавляем строку расхода с отдельными текстами и кнопками
                expenses_list.controls.append(
                    ft.Row(
                        [
                            ft.Text(description, expand=2),  # Название
                            ft.Text(f"{amount} сом", color=amount_color, expand=1, text_align=ft.TextAlign.RIGHT),  # Сумма
                            ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.Colors.BLUE),  # Кнопка редактирования
                            ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.Colors.RED),  # Кнопка удаления
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                )

                total_amount += amount
                total_text.value = f"Общая сумма: {total_amount} сом"

                desc_input.value = ""
                amount_input.value = ""
                page.update()
            else:
                print("Сумма должна быть положительным числом.")
        else:
            print("Введите корректную сумму (например: 1250).")

    # Поля ввода
    desc_input = ft.TextField(label="На что потрачено?", expand=2)
    amount_input = ft.TextField(label="Сколько?", keyboard_type=ft.KeyboardType.NUMBER, expand=1)

    add_button = ft.ElevatedButton(text="Добавить", on_click=add_expense)

    # Верхняя строка с полями ввода и кнопкой
    input_row = ft.Row(
        controls=[desc_input, amount_input, add_button],
        spacing=10,
    )

    # Добавляем всё на страницу
    page.add(
        input_row,
        expenses_list,
        total_text,
    )

ft.app(target=main)
