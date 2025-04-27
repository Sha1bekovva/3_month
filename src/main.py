import flet as ft
import database

def main(page: ft.Page):
    page.title = "Расходы"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Инициализация базы
    database.init_db()

    # Поле для ввода расходов
    title_input = ft.TextField(label="Название расхода", width=300)
    amount_input = ft.TextField(label="Сумма", width=150)

    # Область для списка расходов
    expenses_list_area = ft.Column()

    # Добавить расход
    def add_expense_handler(e):
        title = title_input.value
        try:
            amount = float(amount_input.value)
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Ошибка: сумма должна быть числом!"))
            page.snack_bar.open = True
            page.update()
            return

        if title and amount:
            database.add_expense(title, amount)
            title_input.value = ""
            amount_input.value = ""
            refresh_expenses()
            page.update()

    # Удалить расход
    def delete_expense_handler(e):
        expense_id = e.control.data
        database.delete_expense(expense_id)
        refresh_expenses()
        page.update()

    # Построить список расходов
    def refresh_expenses():
        expenses_list_area.controls.clear()
        expenses = database.get_all_expenses()
        for expense in expenses:
            expenses_list_area.controls.append(
                ft.Row([
                    ft.Text(expense[1], width=200),
                    ft.Text(f"{expense[2]} руб.", width=100),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINED,
                        icon_color=ft.colors.RED,
                        icon_size=20,
                        on_click=delete_expense_handler,
                        data=expense[0],  # ID расхода
                    )
                ])
            )

    # Кнопка добавления
    add_button = ft.ElevatedButton(text="Добавить расход", on_click=add_expense_handler)

    # Главный интерфейс
    page.add(
        ft.Row([title_input, amount_input, add_button]),
        ft.Divider(),
        expenses_list_area
    )

    refresh_expenses()

# Запускаем приложение
ft.app(target=main)
