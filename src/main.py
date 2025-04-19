import flet as ft

def main(page: ft.Page):
    page.title = "Список дел"
    tasks = []
    task_list = ft.Column()

    task_input = ft.TextField(label="Введите задание")

    def add_task(e):
        task = task_input.value.strip()
        if task:
            tasks.append(task)
            print("Текущий список заданий:", tasks)
            task_list.controls.append(ft.Text(task))
            task_input.value = ""
            page.update()

    add_button = ft.ElevatedButton(text="Добавить", on_click=add_task)

    page.add(
        ft.Text("Список дел на день", size=24, weight=ft.FontWeight.BOLD),
        task_input,
        add_button,
        task_list,
    )

ft.app(main)



# дополнительное задание:

import flet as ft

def main(page: ft.Page):
    page.title = "Список друзей"
    friends = []
    friends_list = ft.Column()

    name_input = ft.TextField(label="Имя друга")
    surname_input = ft.TextField(label="Фамилия друга")  # Или замените на "Возраст друга"

    def add_friend(e):
        name = name_input.value.strip()
        surname = surname_input.value.strip()

        if name and surname:
            friend = {"name": name, "surname": surname}
            friends.append(friend)
            print("Список друзей:", friends)

            # Обновляем отображение
            friends_list.controls.append(ft.Text(f"{name} {surname}"))
            name_input.value = ""
            surname_input.value = ""
            page.update()

    add_button = ft.ElevatedButton(text="Добавить друга", on_click=add_friend)

    page.add(
        ft.Text("Добавление друга", size=24, weight=ft.FontWeight.BOLD),
        name_input,
        surname_input,
        add_button,
        ft.Text("Список друзей:", size=20),
        friends_list,
    )

ft.app(main)