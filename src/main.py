import flet as ft

def main(page: ft.Page):
    page.title = "Привет мир"

    # список друзей
    friends = ["Ayzat", "Nurzhan", "Gulina", "Umar", "Juman"]

    # функция, которая вызывается при изменении текста
    def on_text_change(e):
        # получаем значение из поля ввода
        user_input = e.control.value.strip()

        # проверяем, есть ли имя в списке
        if user_input in friends:
            print(f"{user_input} есть в списке!")

    # поле ввода
    name_input = ft.TextField(
        label="Введите имя друга",
        on_change=on_text_change
    )

    # добавляем поле на страницу
    page.add(name_input)

# запускаем приложение
ft.app(main)
