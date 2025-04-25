import flet as ft

def main(page: ft.Page):
    page.title = "Проверка имени"

    # Список имён друзей
    friends = ["Ayzat", "Gulina", "Jumagul", "Jazgul", "Sezim"]

    def change_name(e):
        entered_name = name_input.value.strip()
        if entered_name in friends:
            print(f"{entered_name} есть в списке.")
        else:
            print(f"{entered_name} не найден в списке.")

    name_input = ft.TextField(
        label="Введите ваше имя", on_change=change_name
    )

    page.add(name_input)

ft.app(target=main)
