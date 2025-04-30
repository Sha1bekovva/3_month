import flet as ft
from database import Database


def main(page: ft.Page):
    page.title = "Расходы"
    page.window_width = 800
    page.window_height = 600
    page.data = 0  # для хранения ID редактируемой или удаляемой записи

    db = Database("database.sqlite")
    db.create_tables()

    # Поля для добавления
    todo_input = ft.TextField(label="На что потратили?")
    category_input = ft.TextField(label="Категория")

    # Поля для редактирования (отдельно!)
    edit_todo_input = ft.TextField(label="Изменить расход")
    edit_category_input = ft.TextField(label="Изменить категорию")

    # Список расходов
    todo_list_area = ft.Column(scroll="always", expand=True)

    # Обновление списка из БД
    def update_list():
        todo_list_area.controls.clear()
        for row in db.all_todos():
            todo_list_area.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{row[0]}.", width=30),
                        ft.Text(row[1], width=250),
                        ft.Text(row[2], width=150),
                        ft.IconButton(
                            icon=ft.icons.EDIT,
                            icon_color=ft.colors.BLUE,
                            on_click=open_edit_modal,
                            data=row[0],
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.colors.RED,
                            on_click=open_delete_modal,
                            data=row[0],
                        ),
                    ]
                )
            )
        page.update()

    # Добавление
    def add_todo(e):
        if todo_input.value and category_input.value:
            db.add_todo(todo_input.value, category_input.value)
            todo_input.value = ""
            category_input.value = ""
            update_list()

    # === УДАЛЕНИЕ ===

    def open_delete_modal(e):
        page.data = e.control.data
        page.dialog = delete_modal
        delete_modal.open = True
        page.update()

    def confirm_delete(e):
        db.delete_todo(page.data)
        delete_modal.open = False
        update_list()

    def cancel_delete(e):
        delete_modal.open = False
        page.update()

    delete_modal = ft.AlertDialog(
        title=ft.Text("Удалить расход?"),
        content=ft.Text("Вы уверены, что хотите удалить запись?"),
        actions=[
            ft.ElevatedButton("Удалить", on_click=confirm_delete, bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.OutlinedButton("Отмена", on_click=cancel_delete),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # === РЕДАКТИРОВАНИЕ ===

    def open_edit_modal(e):
        page.data = e.control.data
        todo = db.get_one_todo(page.data)
        edit_todo_input.value = todo[1]
        edit_category_input.value = todo[2]
        page.dialog = edit_modal
        edit_modal.open = True
        page.update()

    def save_edit(e):
        db.update_todo(
            todo_id=page.data,
            todo=edit_todo_input.value,
            category=edit_category_input.value
        )
        edit_modal.open = False
        update_list()

    def cancel_edit(e):
        edit_modal.open = False
        page.update()

    edit_modal = ft.AlertDialog(
        title=ft.Text("Редактировать расход"),
        content=ft.Column([
            edit_todo_input,
            edit_category_input
        ]),
        actions=[
            ft.ElevatedButton("Сохранить", on_click=save_edit, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            ft.OutlinedButton("Отмена", on_click=cancel_edit),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Интерфейс
    form = ft.Row(controls=[todo_input, category_input, ft.ElevatedButton("Добавить", on_click=add_todo)])

    page.add(ft.Text("Учёт расходов", size=30, weight=ft.FontWeight.BOLD))
    page.add(form)
    page.add(todo_list_area)

    update_list()


ft.app(target=main)
