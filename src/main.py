import flet as ft

def main(page: ft.Page):
    page.title = "Список друзей"

    # Пустой список друзей
    friends = []

    def add_friend(e):
        name = name_input.value.strip()
        age = age_input.value.strip()

        if name and age.isdigit():  # Проверяем, что возраст — число
            friend = {"name": name, "age": int(age)}
            friends.append(friend)
            print(f"Список друзей: {friends}")
            name_input.value = ""
            age_input.value = ""
            page.update()
        else:
            print("Введите корректные имя и возраст (возраст должен быть числом).")

    name_input = ft.TextField(label="Имя друга")
    age_input = ft.TextField(label="Возраст друга")
    add_button = ft.ElevatedButton(text="Добавить друга", on_click=add_friend)

    page.add(name_input, age_input, add_button)

ft.app(target=main)
