# main.py
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'horizontal'

    # Боковое меню слева
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.2
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.1, 1  # Тёмный фон для меню
            Rectangle:
                pos: self.pos
                size: self.size

        # Кнопки для меню
        Button:
            text: 'Home'
            background_normal: ''  # Убираем стандартный фон
            background_color: 0.2, 0.6, 0.8, 1
        Button:
            text: 'Settings'
            background_normal: ''
            background_color: 0.2, 0.6, 0.8, 1
        Button:
            text: 'About'
            background_normal: ''
            background_color: 0.2, 0.6, 0.8, 1

    # Основной контент справа
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # Белый фон
            Rectangle:
                pos: self.pos
                size: self.size

        # Иконки и элементы фона
        Label:
            text: 'Your Content Here'
            font_size: '24sp'
            halign: 'center'
        BoxLayout:
            orientation: 'horizontal'
            spacing: 20
            padding: 10

            # Иконки
            Button:
                text: 'Icon 1'
                size_hint: None, None
                size: 80, 80
                background_color: 0.6, 0.2, 0.2, 1
            Button:
                text: 'Icon 2'
                size_hint: None, None
                size: 80, 80
                background_color: 0.2, 0.6, 0.2, 1
            Button:
                text: 'Icon 3'
                size_hint: None, None
                size: 80, 80
                background_color: 0.2, 0.2, 0.6, 1
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    MyApp().run()
